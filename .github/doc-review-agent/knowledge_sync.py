"""
Knowledge-sync linters — terminology and description checks.

Integrated into agent.py to run alongside other rule-based checks.
Requires spacemit-knowledge-sync repo cloned as a sibling to docs-chip.
"""

from __future__ import annotations
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required")

# Read from local copies in the same directory
AGENT_DIR = Path(__file__).resolve().parent
GLOSSARY_PATH = AGENT_DIR / "glossary.yaml"
ENTITIES_DIR = AGENT_DIR / "entities"


def load_glossary() -> list[dict]:
    if not GLOSSARY_PATH.exists():
        return []
    with GLOSSARY_PATH.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def load_entities() -> list[dict]:
    entities = []
    if not ENTITIES_DIR.exists():
        return entities
    for path in sorted(ENTITIES_DIR.glob("*.yaml")):
        with path.open(encoding="utf-8") as f:
            data = yaml.safe_load(f)
        if data:
            entities.append(data)
    return entities


def lang_of(filepath: str) -> str:
    return "zh" if filepath.replace("\\", "/").startswith("zh/") else "en"


def check_terminology(lines: list[str], filepath: str) -> list[tuple[int, str, str]]:
    """Check for forbidden terminology variants."""
    glossary = load_glossary()
    if not glossary:
        return []
    
    lang = lang_of(filepath)
    issues = []
    
    for lineno, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("    "):
            continue
        if re.search(r'^\[.*\]\(.*\)$', stripped) or stripped.startswith("http"):
            continue
        
        clean_line = re.sub(r'`[^`]+`', '', line)
        clean_line = re.sub(r'https?://[^\s]+', '', clean_line)
        clean_line = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', clean_line)
        
        for entry in glossary:
            scope = entry.get("scope", "both")
            if scope != "both" and scope != lang:
                continue
            
            forbidden_key = f"forbidden_{lang}"
            forbidden = entry.get(forbidden_key, [])
            preferred = entry.get(lang) if lang == "zh" else entry.get("term")
            
            if not forbidden or not preferred:
                continue
            
            for variant in forbidden:
                # Support regex patterns (starting with ^)
                if variant.startswith("^"):
                    if re.search(variant, clean_line):
                        issues.append((lineno, "Warning",
                            f"Terminology: prefer `{preferred}` (found forbidden pattern)"))
                        break
                elif variant in clean_line:
                    issues.append((lineno, "Warning",
                        f"Terminology: prefer `{preferred}` instead of `{variant}`"))
                    break
    
    return issues


def check_descriptions(lines: list[str], filepath: str) -> list[tuple[int, str, str]]:
    """Check entity descriptions for attribute drift."""
    entities = load_entities()
    if not entities:
        return []
    
    lang = lang_of(filepath)
    issues = []
    content = "\n".join(lines)
    
    for entity in entities:
        aliases = entity.get("aliases", [])
        if not aliases:
            continue
        
        # Check if any alias appears in content
        found = False
        for alias in aliases:
            pattern = rf"(?<![A-Za-z0-9]){re.escape(alias)}(?![A-Za-z0-9])"
            if re.search(pattern, content, re.IGNORECASE):
                found = True
                break
        
        if not found:
            continue
        
        # Check attributes
        for lineno, line in enumerate(lines, start=1):
            for attr in entity.get("attributes", []):
                canonical = attr.get(f"canonical_{lang}")
                variants = attr.get(f"variants_{lang}", [])
                
                if not canonical or not variants:
                    continue
                
                # Only check lines that mention this attribute
                if not any(v in line for v in variants):
                    continue
                
                if canonical in line:
                    continue
                
                if attr.get("conflict"):
                    issues.append((lineno, "Warning",
                        f"Entity `{entity['entity']}` {attr['key']}: "
                        f"en/zh sources disagree — needs human review"))
                else:
                    found_variants = [v for v in variants if v in line]
                    if found_variants:
                        issues.append((lineno, "Suggestion",
                            f"Entity `{entity['entity']}` {attr['key']}: "
                            f"prefer `{canonical}` (found `{found_variants[0]}`)"))
    
    return issues
