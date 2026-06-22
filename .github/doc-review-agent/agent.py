"""
Doc Review Agent
================
Reviews Markdown documentation files in a pull request and posts
inline comments + a summary to GitHub.

Usage (invoked by GitHub Actions):
    python agent.py

Required environment variables:
    GITHUB_TOKEN       - GitHub token with pull-request write permission
    GITHUB_REPOSITORY  - e.g. "spacemit-com/docs-chip"
    PR_NUMBER          - pull request number
    OPENAI_API_KEY     - (or compatible LLM key)
    OPENAI_BASE_URL    - optional, for compatible endpoints
    OPENAI_MODEL       - model name, e.g. "gpt-4o"
"""

from __future__ import annotations

import os
import re
import sys
import json
import yaml
import pathlib
import textwrap
import requests
from dataclasses import dataclass, field
from typing import Literal

# ─── Configuration ────────────────────────────────────────────────────────────

REPO          = os.environ["GITHUB_REPOSITORY"]          # "owner/repo"
PR_NUMBER     = int(os.environ["PR_NUMBER"])
GITHUB_TOKEN  = os.environ["GITHUB_TOKEN"]
LLM_API_KEY   = os.environ.get("OPENAI_API_KEY", "")
LLM_BASE_URL  = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
LLM_MODEL     = os.environ.get("OPENAI_MODEL", "gpt-4o")

CONFIG_PATH   = pathlib.Path(__file__).parent / "config.yml"
PROMPT_PATH   = pathlib.Path(__file__).parent / "system_prompt.md"
WORKSPACE     = pathlib.Path(os.environ.get("GITHUB_WORKSPACE", "."))

GH_API        = "https://api.github.com"
GH_HEADERS    = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}

# ─── Data types ───────────────────────────────────────────────────────────────

Severity = Literal["Error", "Warning", "Suggestion", "错误", "警告", "建议"]

@dataclass
class ReviewComment:
    path: str           # relative file path
    line: int           # 1-based line number in the file
    body: str           # comment text (already formatted)
    severity: str       # Error / Warning / Suggestion


@dataclass
class ReviewResult:
    comments: list[ReviewComment] = field(default_factory=list)
    errors: int = 0
    warnings: int = 0
    suggestions: int = 0


# ─── GitHub helpers ───────────────────────────────────────────────────────────

def gh_get(path: str) -> dict | list:
    r = requests.get(f"{GH_API}{path}", headers=GH_HEADERS, timeout=30)
    r.raise_for_status()
    return r.json()


def gh_post(path: str, body: dict) -> dict:
    r = requests.post(f"{GH_API}{path}", headers=GH_HEADERS, json=body, timeout=30)
    r.raise_for_status()
    return r.json()


def get_pr_files() -> list[dict]:
    """Return list of changed files in the PR (up to 300 files)."""
    files = []
    page = 1
    while True:
        batch = gh_get(f"/repos/{REPO}/pulls/{PR_NUMBER}/files?per_page=100&page={page}")
        if not batch:
            break
        files.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return files


def get_pr_head_sha() -> str:
    pr = gh_get(f"/repos/{REPO}/pulls/{PR_NUMBER}")
    return pr["head"]["sha"]


def get_pr_info() -> dict:
    """Return the full PR object (title, body, head sha, etc.)."""
    return gh_get(f"/repos/{REPO}/pulls/{PR_NUMBER}")


def update_pr_description(new_body: str) -> None:
    """Prepend the auto-generated summary block to the PR description."""
    import requests as _req
    r = _req.patch(
        f"{GH_API}/repos/{REPO}/pulls/{PR_NUMBER}",
        headers=GH_HEADERS,
        json={"body": new_body},
        timeout=30,
    )
    r.raise_for_status()


def post_review(comments: list[ReviewComment], summary_body: str, commit_sha: str) -> None:
    """Post all inline comments + summary as a single PR review."""
    gh_comments = []
    for c in comments:
        gh_comments.append({
            "path": c.path,
            "line": c.line,
            "side": "RIGHT",
            "body": c.body,
        })

    payload = {
        "commit_id": commit_sha,
        "body": summary_body,
        "event": "COMMENT",      # advisory only — never REQUEST_CHANGES
        "comments": gh_comments,
    }
    gh_post(f"/repos/{REPO}/pulls/{PR_NUMBER}/reviews", payload)


# ─── Rule-based checks ────────────────────────────────────────────────────────

def is_zh(filepath: str) -> bool:
    return filepath.startswith("zh/")


def label(sev: str, zh: bool) -> str:
    mapping = {
        "Error":      "错误" if zh else "Error",
        "Warning":    "警告" if zh else "Warning",
        "Suggestion": "建议" if zh else "Suggestion",
    }
    return f"`[{mapping.get(sev, sev)}]`"


def check_frontmatter(content: str, path: str, cfg: dict) -> list[tuple[int, str, str]]:
    """
    Returns list of (line, severity, message).

    This repo uses a bare single-line frontmatter format (no --- delimiters):

        sidebar_position: 2

        # Section Title

    A YAML --- block is NOT used and should NOT be flagged as valid.
    We accept either format defensively, but the canonical form is bare.
    """
    issues = []
    first_line = content.split("\n", 1)[0].strip()

    # --- YAML block format (not canonical here, but accept it)
    if content.startswith("---"):
        end = content.find("\n---", 3)
        if end == -1:
            issues.append((1, "Warning", "Frontmatter `---` block is not closed."))
            return issues
        try:
            fm = yaml.safe_load(content[3:end])
        except yaml.YAMLError:
            issues.append((1, "Error", "Frontmatter YAML is invalid."))
            return issues
        if not isinstance(fm, dict):
            return issues
        for field_name in cfg.get("required_fields", ["sidebar_position"]):
            if field_name not in fm:
                issues.append((1, "Warning",
                    f"Frontmatter is missing required field: `{field_name}`."))
        return issues

    # Bare single-line format: "sidebar_position: <int>"
    bare_fm = re.match(r'^sidebar_position\s*:\s*(\d+)', first_line)
    if bare_fm:
        # Valid — check for required fields beyond sidebar_position
        for field_name in cfg.get("required_fields", ["sidebar_position"]):
            if field_name != "sidebar_position":
                # Other required fields can't be in bare format; flag only if really missing
                issues.append((1, "Warning",
                    f"Frontmatter is missing required field: `{field_name}`."))
        return issues

    # Neither format found
    issues.append((1, "Warning",
        "Missing `sidebar_position` frontmatter. "
        "Add `sidebar_position: N` as the first line of the file "
        "(no `---` delimiters needed)."))
    return issues


def check_headings(lines: list[str]) -> list[tuple[int, str, str]]:
    issues = []
    prev_level = 0
    for i, line in enumerate(lines, 1):
        m = re.match(r'^(#{1,6})\s', line)
        if not m:
            continue
        level = len(m.group(1))
        if prev_level > 0 and level > prev_level + 1:
            issues.append((i, "Warning",
                f"Heading level jumps from `{'#' * prev_level}` to `{'#' * level}`. "
                "Avoid skipping heading levels."))
        prev_level = level
    return issues


def check_tbd(lines: list[str]) -> list[tuple[int, str, str]]:
    issues = []
    pattern = re.compile(r'\b(TBD|TODO|FIXME)\b', re.IGNORECASE)
    for i, line in enumerate(lines, 1):
        if pattern.search(line):
            issues.append((i, "Warning",
                f"Found `{pattern.search(line).group()}` placeholder. "
                "Remove or replace before publication."))
    return issues


def check_images(lines: list[str], file_path: str) -> list[tuple[int, str, str]]:
    issues = []
    img_pattern = re.compile(r'!\[.*?\]\(([^)]+)\)')
    base_dir = (WORKSPACE / file_path).parent

    for i, line in enumerate(lines, 1):
        for m in img_pattern.finditer(line):
            img_src = m.group(1)
            if img_src.startswith("http"):
                continue
            img_path = (base_dir / img_src).resolve()
            if not img_path.exists():
                issues.append((i, "Error",
                    f"Image not found: `{img_src}`. "
                    "Add the file to the `static/` directory or fix the path."))
    return issues


def check_links(lines: list[str], file_path: str) -> list[tuple[int, str, str]]:
    issues = []
    link_pattern = re.compile(r'\[.*?\]\(([^)#]+)(?:#[^)]*)?\)')
    base_dir = (WORKSPACE / file_path).parent

    for i, line in enumerate(lines, 1):
        for m in link_pattern.finditer(line):
            target = m.group(1).strip()
            if target.startswith("http"):
                continue
            target_path = (base_dir / target).resolve()
            if not target_path.exists():
                issues.append((i, "Error",
                    f"Broken link: `{target}`. "
                    "Verify the target file exists or update the path."))
    return issues


def check_links_to_deleted(all_md_files: list[pathlib.Path],
                           deleted_paths: set[str]) -> list[tuple[str, int, str, str]]:
    """
    Scan every tracked Markdown file for links that now point to a file
    deleted/renamed in this PR.
    Returns list of (file_path, line, severity, message).
    """
    if not deleted_paths:
        return []

    link_pattern = re.compile(r'\[.*?\]\(([^)#]+)(?:#[^)]*)?\)')
    results: list[tuple[str, int, str, str]] = []

    for md_file in all_md_files:
        try:
            rel = md_file.relative_to(WORKSPACE).as_posix()
        except ValueError:
            continue
        try:
            lines = md_file.read_text(encoding="utf-8").splitlines()
        except Exception:
            continue
        base_dir = md_file.parent
        for i, line in enumerate(lines, 1):
            for m in link_pattern.finditer(line):
                target = m.group(1).strip()
                if target.startswith("http"):
                    continue
                resolved = (base_dir / target).resolve()
                try:
                    resolved_rel = resolved.relative_to(WORKSPACE.resolve()).as_posix()
                except ValueError:
                    continue
                if resolved_rel in deleted_paths:
                    results.append((rel, i, "Error",
                        f"Link `{target}` points to `{resolved_rel}` which was "
                        "deleted or renamed in this PR. Update or remove the link."))
    return results


def check_code_blocks(lines: list[str]) -> list[tuple[int, str, str]]:
    issues = []
    for i, line in enumerate(lines, 1):
        if re.match(r'^```\s*$', line):
            issues.append((i, "Suggestion",
                "Code block has no language identifier. "
                "Specify a language (e.g., ` ```bash `, ` ```c `) for syntax highlighting."))
    return issues


def check_chinese_punctuation(lines: list[str], path: str) -> list[tuple[int, str, str]]:
    if not is_zh(path):
        return []
    issues = []
    # Detect common ASCII punctuation in prose (outside code blocks)
    in_code = False
    ascii_punct = re.compile(r'(?<!\s)[,;:](?!\s*\d)')  # rough heuristic
    for i, line in enumerate(lines, 1):
        if line.startswith("```"):
            in_code = not in_code
        if in_code:
            continue
        if ascii_punct.search(line):
            issues.append((i, "Suggestion",
                "检测到 ASCII 标点符号（`,` `;` `:`）。中文文档请使用中文标点（，；：）。"))
    return issues


def check_consecutive_blank_lines(lines: list[str]) -> list[tuple[int, str, str]]:
    """Flag runs of more than 2 consecutive blank lines."""
    issues = []
    blank_run = 0
    run_start = 0
    for i, line in enumerate(lines, 1):
        if line.strip() == "":
            if blank_run == 0:
                run_start = i
            blank_run += 1
        else:
            if blank_run > 2:
                issues.append((run_start, "Suggestion",
                    f"{blank_run} consecutive blank lines found. "
                    "Reduce to at most 1 blank line between paragraphs."))
            blank_run = 0
    return issues


def check_trailing_whitespace(lines: list[str]) -> list[tuple[int, str, str]]:
    """Flag lines with trailing spaces (except intentional line-break double-space)."""
    issues = []
    for i, line in enumerate(lines, 1):
        stripped = line.rstrip("\n")
        if stripped.endswith(" ") and not stripped.endswith("  "):  # single trailing space
            issues.append((i, "Suggestion",
                "Trailing whitespace detected. Remove the trailing space(s)."))
    return issues


def check_table_structure(lines: list[str]) -> list[tuple[int, str, str]]:
    """Check that Markdown tables have a separator row and consistent column counts."""
    issues = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r'^\s*\|', line):
            # Collect table block
            table_start = i + 1  # 1-based
            col_counts = []
            j = i
            while j < len(lines) and (re.match(r'^\s*\|', lines[j]) or lines[j].strip() == ""):
                if re.match(r'^\s*\|', lines[j]):
                    col_counts.append(lines[j].count("|"))
                j += 1

            if len(col_counts) >= 2:
                # Second row must be a separator (only |, -, :, space)
                sep_row = lines[i + 1] if i + 1 < len(lines) else ""
                if not re.match(r'^[\s|:\-]+$', sep_row):
                    issues.append((table_start + 1, "Error",
                        "Table is missing a separator row (`| --- | --- |`) after the header."))
                # Check consistent column count (ignore separator row)
                data_cols = [c for idx, c in enumerate(col_counts) if idx != 1]
                if len(set(data_cols)) > 1:
                    issues.append((table_start, "Warning",
                        "Table has inconsistent column counts across rows. "
                        "Ensure every row has the same number of `|` delimiters."))
            i = j
        else:
            i += 1
    return issues


def check_product_name_casing(lines: list[str]) -> list[tuple[int, str, str]]:
    """Flag incorrect casing of product names (K1, K3, P1, P1S)."""
    issues = []
    # Match variants like k1, K-1, k-1, p1s, P-1S, etc. but not the correct forms
    wrong = re.compile(r'\b(k1|k3|p1s|p1|K-1|K-3|P-1S|P-1)\b')
    correct_forms = {"k1": "K1", "k3": "K3", "p1s": "P1S", "p1": "P1",
                     "K-1": "K1", "K-3": "K3", "P-1S": "P1S", "P-1": "P1"}
    in_code = False
    for i, line in enumerate(lines, 1):
        if line.startswith("```"):
            in_code = not in_code
        if in_code:
            continue
        for m in wrong.finditer(line):
            token = m.group()
            correct = correct_forms.get(token, token.upper().replace("-", ""))
            issues.append((i, "Warning",
                f"Incorrect product name casing: `{token}`. Use `{correct}`."))
    return issues


def check_missing_units(lines: list[str]) -> list[tuple[int, str, str]]:
    """Flag bare numeric values that are likely missing units."""
    issues = []
    # Match numbers followed by nothing, or a non-unit word — heuristic
    # Patterns: a standalone number at end of sentence or before punctuation
    bare_num = re.compile(
        r'(?<![\w/])'
        r'(\d+\.?\d*)'
        r'(?!\s*(?:V|mV|A|mA|MHz|GHz|kHz|Hz|°C|℃|KB|MB|GB|TB|ns|us|ms|s|Ω|W|mW|%|\.|,|\d))'
        r'(?=[\s,\.;。，])'
    )
    unit_context = re.compile(
        r'(?i)(voltage|current|frequen|temperatur|speed|capacity|power|resistanc|timing|latency)'
    )
    in_code = False
    for i, line in enumerate(lines, 1):
        if line.startswith("```"):
            in_code = not in_code
        if in_code:
            continue
        if unit_context.search(line):
            for m in bare_num.finditer(line):
                issues.append((i, "Suggestion",
                    f"Numeric value `{m.group(1)}` appears to be missing a unit "
                    "(e.g., V, mA, MHz, °C). Add the appropriate unit."))
    return issues


def check_first_person(lines: list[str], file_path: str) -> list[tuple[int, str, str]]:
    """Flag first-person pronouns in en/ formal documentation."""
    if is_zh(file_path):
        return []
    issues = []
    # Only flag unambiguous personal pronouns; exclude 'our' in company/product context
    pattern = re.compile(r'\b(I|my|me|we|us)\b')
    in_code = False
    for i, line in enumerate(lines, 1):
        if line.startswith("```"):
            in_code = not in_code
        if in_code or line.startswith(">") or line.startswith("#"):
            continue
        for m in pattern.finditer(line):
            found = m.group()
            issues.append((i, "Warning",
                f"First-person pronoun `{found}` is not appropriate in formal technical "
                "documentation. Rewrite using imperative mood or a subject-neutral construction "
                "(e.g., \"The user should…\" or \"Configure the…\")."))
    return issues


def check_passive_overuse(lines: list[str], file_path: str) -> list[tuple[int, str, str]]:
    """Passive voice is acceptable and natural in academic/formal technical EN docs.
    This check is intentionally a no-op; kept for config compatibility."""
    return []
    return issues


def check_admonition_keywords(lines: list[str], file_path: str) -> list[tuple[int, str, str]]:
    """Flag non-standard admonition keywords (NOTE/WARNING/CAUTION/TIP only)."""
    issues = []
    # Match blockquote lines that start with bold keyword
    admon = re.compile(r'^>\s*\*\*(\w[\w\s]*)\*\*')
    valid_en = {"NOTE", "WARNING", "CAUTION", "TIP", "IMPORTANT"}
    valid_zh = {"注意", "警告", "提示", "重要", "危险"}
    valid = valid_zh if is_zh(file_path) else valid_en
    for i, line in enumerate(lines, 1):
        m = admon.match(line)
        if m:
            kw = m.group(1).strip().upper() if not is_zh(file_path) else m.group(1).strip()
            if kw not in valid and kw not in {v.upper() for v in valid}:
                allowed = "、".join(sorted(valid)) if is_zh(file_path) else ", ".join(sorted(valid))
                issues.append((i, "Suggestion",
                    f"Non-standard admonition keyword `{m.group(1).strip()}`. "
                    f"Use one of: {allowed}."))
    return issues


def check_bilingual_pair(file_path: str) -> list[tuple[int, str, str]]:
    issues = []
    if file_path.startswith("en/"):
        pair = "zh/" + file_path[3:]
    elif file_path.startswith("zh/"):
        pair = "en/" + file_path[3:]
    else:
        return issues

    pair_full = WORKSPACE / pair
    if not pair_full.exists():
        issues.append((1, "Warning",
            f"Bilingual counterpart not found: `{pair}`. "
            "Create the corresponding file or update the language index."))
    return issues


def build_translation_sync_table(pr_files: list[dict]) -> str:
    """
    Build a Markdown table listing every changed doc file whose bilingual
    counterpart was NOT also changed in this PR.
    Returns an empty string if everything is in sync.
    """
    md_files = [f["filename"] for f in pr_files
                if f.get("status") != "removed"
                and (f["filename"].startswith("en/") or f["filename"].startswith("zh/"))
                and f["filename"].endswith(".md")]
    pr_paths = set(md_files)

    out_of_sync: list[tuple[str, str, str]] = []  # (changed, counterpart, exists_on_disk)
    seen: set[str] = set()

    for fpath in md_files:
        if fpath in seen:
            continue
        if fpath.startswith("en/"):
            pair = "zh/" + fpath[3:]
        else:
            pair = "en/" + fpath[3:]

        if pair not in pr_paths:
            exists = "✅ exists" if (WORKSPACE / pair).exists() else "❌ missing"
            out_of_sync.append((fpath, pair, exists))
        seen.add(fpath)
        seen.add(pair)

    if not out_of_sync:
        return ""

    rows = "\n".join(
        f"| `{changed}` | `{counterpart}` | {status} |"
        for changed, counterpart, status in out_of_sync
    )
    return (
        "### 🌐 Translation Sync\n\n"
        "The following files were changed without updating their language counterpart:\n\n"
        "| Changed file | Counterpart not in PR | Counterpart on disk |\n"
        "|---|---|---|\n"
        f"{rows}\n"
    )


def check_bilingual_sync(file_path: str, pr_file_paths: set[str]) -> list[tuple[int, str, str]]:
    """
    If this file was modified in the PR but its language counterpart was NOT,
    remind the author to update the paired file to keep both versions in sync.
    Only fires when the counterpart file actually exists on disk.
    """
    issues = []
    if file_path.startswith("en/"):
        pair = "zh/" + file_path[3:]
    elif file_path.startswith("zh/"):
        pair = "en/" + file_path[3:]
    else:
        return issues

    pair_full = WORKSPACE / pair
    if not pair_full.exists():
        return issues   # missing pair is handled by check_bilingual_pair

    if pair not in pr_file_paths:
        lang = "英文" if file_path.startswith("zh/") else "Chinese"
        pair_lang = "Chinese" if file_path.startswith("en/") else "英文"
        if file_path.startswith("zh/"):
            issues.append((1, "Warning",
                f"此文件已在本 PR 中修改，但对应的{lang}文档 `{pair}` 未同步更新。"
                "请同步修改对应文档，确保中英文内容一致。"))
        else:
            issues.append((1, "Warning",
                f"This file was updated in this PR but its {pair_lang} counterpart `{pair}` "
                "was not. Update the paired file to keep both language versions in sync."))
    return issues


# ─── LLM-assisted review ─────────────────────────────────────────────────────

def llm_review(content: str, file_path: str, system_prompt: str) -> list[tuple[int, str, str]]:
    """
    Ask the LLM to review the document content.
    Returns list of (line, severity, message).
    """
    if not LLM_API_KEY:
        return []

    lang_hint = "This file is under zh/ — respond in Chinese." if is_zh(file_path) else \
                "This file is under en/ — respond in English."

    user_msg = textwrap.dedent(f"""
        Review the following Markdown file: `{file_path}`
        {lang_hint}

        Return your findings as a JSON array. Each item must have:
        - "line": integer (1-based line number closest to the issue)
        - "severity": "Error" | "Warning" | "Suggestion"  (use Chinese equivalents for zh/ files)
        - "message": string (formatted per the style guide in your system prompt)

        If there are no issues, return an empty array [].

        ```markdown
        {content[:12000]}
        ```
    """).strip()

    payload = {
        "model": LLM_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_msg},
        ],
        "temperature": 0.1,
        "response_format": {"type": "json_object"},
    }

    try:
        r = requests.post(
            f"{LLM_BASE_URL}/chat/completions",
            headers={"Authorization": f"Bearer {LLM_API_KEY}", "Content-Type": "application/json"},
            json=payload,
            timeout=60,
        )
        r.raise_for_status()
        raw = r.json()["choices"][0]["message"]["content"]
        data = json.loads(raw)
        items = data if isinstance(data, list) else data.get("issues", data.get("findings", []))
        return [(int(item["line"]), item["severity"], item["message"]) for item in items]
    except Exception as e:
        print(f"  LLM review failed for {file_path}: {e}", file=sys.stderr)
        return []


# ─── Main ─────────────────────────────────────────────────────────────────────

def run_checks(file_path: str, content: str, cfg: dict,
               pr_file_paths: set[str] | None = None) -> list[tuple[int, str, str]]:
    lines = content.splitlines()
    issues: list[tuple[int, str, str]] = []
    if pr_file_paths is None:
        pr_file_paths = set()

    if cfg["checks"]["frontmatter"]["enabled"]:
        issues += check_frontmatter(content, file_path, cfg["checks"]["frontmatter"])
    if cfg["checks"]["heading_hierarchy"]["enabled"]:
        issues += check_headings(lines)
    if cfg["checks"]["technical_style"]["enabled"] and cfg["checks"]["technical_style"]["flag_tbd"]:
        issues += check_tbd(lines)
    if cfg["checks"]["missing_images"]["enabled"]:
        issues += check_images(lines, file_path)
    if cfg["checks"]["broken_links"]["enabled"]:
        issues += check_links(lines, file_path)
    if cfg["checks"]["technical_style"]["enabled"] and cfg["checks"]["technical_style"]["flag_code_block_language"]:
        issues += check_code_blocks(lines)
    if cfg["checks"]["punctuation"]["enabled"] and cfg["checks"]["punctuation"]["chinese_punctuation_in_zh"]:
        issues += check_chinese_punctuation(lines, file_path)
    if cfg["checks"]["bilingual_mirror"]["enabled"] and cfg["checks"]["bilingual_mirror"]["flag_missing_pair"]:
        issues += check_bilingual_pair(file_path)
    if cfg["checks"]["bilingual_mirror"]["enabled"] and cfg["checks"]["bilingual_mirror"].get("flag_sync_reminder", True):
        issues += check_bilingual_sync(file_path, pr_file_paths)

    # ── New professional technical-writer checks ──────────────────────────────
    tw = cfg["checks"].get("technical_writing", {})

    if tw.get("consecutive_blank_lines", {}).get("enabled", True):
        issues += check_consecutive_blank_lines(lines)

    if tw.get("trailing_whitespace", {}).get("enabled", True):
        issues += check_trailing_whitespace(lines)

    if tw.get("table_structure", {}).get("enabled", True):
        issues += check_table_structure(lines)

    if tw.get("product_name_casing", {}).get("enabled", True):
        issues += check_product_name_casing(lines)

    if tw.get("missing_units", {}).get("enabled", True):
        issues += check_missing_units(lines)

    if tw.get("first_person", {}).get("enabled", True):
        issues += check_first_person(lines, file_path)

    if tw.get("passive_voice", {}).get("enabled", True):
        issues += check_passive_overuse(lines, file_path)

    if tw.get("admonition_keywords", {}).get("enabled", True):
        issues += check_admonition_keywords(lines, file_path)

    return issues


def build_comment_body(sev: str, message: str, zh: bool) -> str:
    lbl = label(sev, zh)
    return f"{lbl} {message}\n\n<!-- bot:doc-review -->"


def build_pr_description_block(pr_files: list[dict]) -> str:
    """
    Auto-generate a structured summary block describing what changed in this PR.
    Covers: which chips, which doc types, EN/ZH or both.
    """
    chip_map = {"k1": "K1", "k3": "K3", "p1s": "P1S", "p1": "P1"}
    doctype_map = {
        "_usermanual": "User Manual",
        "_hw": "Hardware Design",
        "_sw": "Software / SDK",
        "_docs": "Product Docs",
        "_ds": "Datasheet",
        "_hw_faq": "HW FAQ",
        "_sw_faq": "SW FAQ",
    }

    chips: set[str] = set()
    doctypes: set[str] = set()
    langs: set[str] = set()
    added = added_count = 0
    modified = modified_count = 0
    removed_count = 0

    for f in pr_files:
        fpath = f["filename"]
        status = f.get("status", "modified")

        if not fpath.endswith(".md"):
            continue

        if fpath.startswith("en/"):
            langs.add("EN")
        elif fpath.startswith("zh/"):
            langs.add("ZH")

        parts = fpath.lower().split("/")
        for part in parts:
            for key, label in chip_map.items():
                if part == key or part.startswith(key + "_") or part.startswith(key + "/"):
                    chips.add(label)
        for part in parts:
            for key, label in doctype_map.items():
                if key in part:
                    doctypes.add(label)

        if status == "added":
            added_count += 1
        elif status == "removed":
            removed_count += 1
        else:
            modified_count += 1

    chips_str = ", ".join(sorted(chips)) if chips else "—"
    doctypes_str = ", ".join(sorted(doctypes)) if doctypes else "—"
    langs_str = " + ".join(sorted(langs)) if langs else "—"

    change_parts = []
    if added_count:
        change_parts.append(f"{added_count} added")
    if modified_count:
        change_parts.append(f"{modified_count} modified")
    if removed_count:
        change_parts.append(f"{removed_count} removed")
    changes_str = ", ".join(change_parts) if change_parts else "no changes"

    return textwrap.dedent(f"""
        <!-- bot:doc-review:description -->
        ## 📝 Auto-generated PR Summary

        | Field       | Value |
        |-------------|-------|
        | Chips       | {chips_str} |
        | Doc types   | {doctypes_str} |
        | Languages   | {langs_str} |
        | Files       | {changes_str} |

        > *Generated by doc-review-agent. Edit below this block to add context.*
        <!-- /bot:doc-review:description -->
    """).strip()


def update_pr_description_with_summary(pr_info: dict, pr_files: list[dict]) -> None:
    """
    Prepend (or replace) the auto-summary block in the PR description.
    Preserves any human-written content that follows the block.
    """
    block = build_pr_description_block(pr_files)
    existing_body = pr_info.get("body") or ""

    # Strip previous auto-block if present
    start_marker = "<!-- bot:doc-review:description -->"
    end_marker = "<!-- /bot:doc-review:description -->"
    if start_marker in existing_body and end_marker in existing_body:
        s = existing_body.index(start_marker)
        e = existing_body.index(end_marker) + len(end_marker)
        existing_body = (existing_body[:s] + existing_body[e:]).strip()

    new_body = block + ("\n\n" + existing_body if existing_body else "")
    update_pr_description(new_body)


def build_summary(result: ReviewResult, zh: bool,
                  sync_table: str = "") -> str:
    bot_tag = "<!-- bot:doc-review -->"
    sync_section = ("\n\n" + sync_table.strip()) if sync_table else ""
    if zh:
        return textwrap.dedent(f"""
            ## 📋 文档审阅摘要

            | 级别 | 数量 |
            |------|------|
            | 错误 | {result.errors} |
            | 警告 | {result.warnings} |
            | 建议 | {result.suggestions} |

            > 错误项表示信息缺失或有误，建议在合并前处理。
            > 警告和建议仅供参考，最终合并决策由人工审阅者决定。
            {sync_section}
            {bot_tag}
        """).strip()
    else:
        return textwrap.dedent(f"""
            ## 📋 Doc Review Summary

            | Severity   | Count |
            |------------|-------|
            | Error      | {result.errors} |
            | Warning    | {result.warnings} |
            | Suggestion | {result.suggestions} |

            > Errors indicate missing or incorrect information that should be addressed before merge.
            > Warnings and suggestions are advisory — human reviewer makes the final call.
            {sync_section}
            {bot_tag}
        """).strip()


def main() -> None:
    cfg = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    system_prompt = PROMPT_PATH.read_text(encoding="utf-8")

    pr_files = get_pr_files()
    pr_info = get_pr_info()
    commit_sha = pr_info["head"]["sha"]

    # Filter to Markdown doc files only
    include_re = [re.compile(p.replace("**", ".*").replace("*", "[^/]*"))
                  for p in cfg["include_patterns"]]
    exclude_re = [re.compile(p.replace("**", ".*").replace("*", "[^/]*"))
                  for p in cfg.get("exclude_patterns", [])]

    def is_included(path: str) -> bool:
        return (any(r.fullmatch(path) for r in include_re) and
                not any(r.fullmatch(path) for r in exclude_re))

    # ── Item 5: Auto-update PR description ───────────────────────────────────
    print("Updating PR description with auto-summary...")
    try:
        update_pr_description_with_summary(pr_info, pr_files)
    except Exception as e:
        print(f"  PR description update failed (non-fatal): {e}", file=sys.stderr)

    # ── Item 2: Check links pointing to deleted/renamed files ─────────────────
    deleted_paths = {
        f["filename"] for f in pr_files
        if f.get("status") in ("removed", "renamed")
    }
    all_md_files = list(WORKSPACE.rglob("*.md"))
    dangling_link_issues = check_links_to_deleted(all_md_files, deleted_paths)

    result = ReviewResult()
    all_comments: list[ReviewComment] = []
    has_zh = False

    # Add dangling-link issues as review comments
    for fpath, line_no, sev, msg in dangling_link_issues:
        zh = is_zh(fpath)
        if zh:
            has_zh = True
        body = build_comment_body(sev, msg, zh)
        all_comments.append(ReviewComment(path=fpath, line=line_no, body=body, severity=sev))
        if sev.lower() in ("error", "错误"):
            result.errors += 1
        elif sev.lower() in ("warning", "警告"):
            result.warnings += 1
        else:
            result.suggestions += 1

    for f in pr_files:
        fpath = f["filename"]
        status = f.get("status", "")

        if not is_included(fpath):
            continue
        if status == "removed":
            continue

        print(f"Reviewing: {fpath}")
        zh = is_zh(fpath)
        if zh:
            has_zh = True

        full_path = WORKSPACE / fpath
        try:
            content = full_path.read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"  File not found locally, skipping: {fpath}", file=sys.stderr)
            continue

        # Rule-based checks
        pr_paths = {f["filename"] for f in pr_files}
        issues = run_checks(fpath, content, cfg, pr_file_paths=pr_paths)

        # LLM-assisted checks
        llm_issues = llm_review(content, fpath, system_prompt)
        issues += llm_issues

        for line_no, sev, msg in issues:
            body = build_comment_body(sev, msg, zh)
            all_comments.append(ReviewComment(path=fpath, line=line_no, body=body, severity=sev))

            sev_norm = sev.lower()
            if sev_norm in ("error", "错误"):
                result.errors += 1
            elif sev_norm in ("warning", "警告"):
                result.warnings += 1
            else:
                result.suggestions += 1

    # ── Item 1: Build PR-level translation sync table for the summary ─────────
    sync_table = build_translation_sync_table(pr_files)

    summary = build_summary(result, zh=has_zh, sync_table=sync_table)

    if all_comments or result.errors + result.warnings + result.suggestions > 0:
        print(f"\nPosting review: {result.errors} errors, {result.warnings} warnings, "
              f"{result.suggestions} suggestions")
        post_review(all_comments, summary, commit_sha)
    else:
        print("No issues found. Posting clean summary.")
        post_review([], summary, commit_sha)


if __name__ == "__main__":
    main()
