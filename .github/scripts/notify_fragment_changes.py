#!/usr/bin/env python3
"""Detect fragment value changes and create GitHub issues for downstream updates.

Compares current fragment values against baseline, opens an issue listing
all downstream files that need updating when a canonical value changes.
"""

import os
import sys
import json
import subprocess
from pathlib import Path

import yaml
import requests

REPO = os.environ["GITHUB_REPOSITORY"]
TOKEN = os.environ["GITHUB_TOKEN"]
FRAGMENTS_REPO = "junlin-luo-spacemit/spacemit-knowledge-sync"
FRAGMENTS_BRANCH = "master"


def fetch_fragments():
    """Fetch current fragment registry from spacemit-knowledge-sync."""
    url = f"https://api.github.com/repos/{FRAGMENTS_REPO}/contents/fragments"
    headers = {"Authorization": f"token {TOKEN}"}
    resp = requests.get(url, headers=headers, params={"ref": FRAGMENTS_BRANCH})
    resp.raise_for_status()
    
    fragments = {}
    for item in resp.json():
        if not item["name"].endswith(".yaml"):
            continue
        
        file_resp = requests.get(item["download_url"])
        file_resp.raise_for_status()
        data = yaml.safe_load(file_resp.text)
        
        chip = data.get("chip", "?")
        subsystem = data.get("subsystem")
        key = f"{chip}_{subsystem}" if subsystem else chip
        
        fragments[key] = data
    
    return fragments


def get_changed_files():
    """Get list of files changed in the current commit."""
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout.strip().split("\n")


def detect_value_changes(fragments, changed_files):
    """Detect which fragment values changed based on file content diff."""
    changes = []
    
    for file_path in changed_files:
        if not file_path.endswith(".md"):
            continue
        if not any(x in file_path for x in ["_ds.md", "root_overview.md"]):
            continue
        
        # Get diff for this file
        try:
            result = subprocess.run(
                ["git", "diff", "HEAD~1", "HEAD", "--", file_path],
                capture_output=True,
                text=True,
                check=True
            )
            diff = result.stdout
        except subprocess.CalledProcessError:
            continue
        
        # Scan all fragments for values that appear in removed lines
        for frag_key, frag_data in fragments.items():
            for key, spec in frag_data.get("fragments", {}).items():
                canonical_en = spec.get("canonical_en") or spec.get("canonical", "")
                canonical_zh = spec.get("canonical_zh") or spec.get("canonical", "")
                
                for canonical in [str(canonical_en), str(canonical_zh)]:
                    if not canonical:
                        continue
                    
                    # Check if this value was removed (old value)
                    if f"-{canonical}" in diff or f"- {canonical}" in diff:
                        # And a different value was added (new value)
                        added_lines = [l for l in diff.split("\n") if l.startswith("+") and not l.startswith("+++")]
                        
                        for line in added_lines:
                            if canonical not in line:  # Different value added
                                changes.append({
                                    "chip": frag_data.get("chip"),
                                    "subsystem": frag_data.get("subsystem"),
                                    "fragment": key,
                                    "old_value": canonical,
                                    "file": file_path,
                                    "used_in": spec.get("used_in", [])
                                })
                                break
    
    return changes


def create_issue(changes):
    """Create a GitHub issue listing files that need updates."""
    if not changes:
        return
    
    # Group by fragment
    by_fragment = {}
    for change in changes:
        fkey = f"{change['chip']}/{change['fragment']}"
        if fkey not in by_fragment:
            by_fragment[fkey] = change
    
    title = "Fragment value changed: update downstream files"
    body_parts = ["⚠️ **Fragment registry detected value changes**\n"]
    
    for fkey, change in by_fragment.items():
        subsys = f" ({change['subsystem']})" if change.get("subsystem") else ""
        body_parts.append(f"\n## {change['chip']}{subsys} / `{change['fragment']}`\n")
        body_parts.append(f"Changed in: `{change['file']}`\n")
        body_parts.append(f"Old value: `{change['old_value']}`\n")
        body_parts.append(f"\n**{len(change['used_in'])} downstream files need updating:**\n")
        
        for ref in change["used_in"][:20]:  # Limit to first 20
            body_parts.append(f"- `{ref}`\n")
        
        if len(change["used_in"]) > 20:
            body_parts.append(f"- _(and {len(change['used_in']) - 20} more)_\n")
    
    body_parts.append("\n---\n")
    body_parts.append("Run `python scripts/lint_fragments.py --impact <fragment>` in ")
    body_parts.append("[spacemit-knowledge-sync](https://github.com/junlin-luo-spacemit/spacemit-knowledge-sync) ")
    body_parts.append("for full impact analysis.")
    
    body = "".join(body_parts)
    
    url = f"https://api.github.com/repos/{REPO}/issues"
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "title": title,
        "body": body,
        "labels": ["documentation", "sync-required"]
    }
    
    resp = requests.post(url, headers=headers, json=data)
    resp.raise_for_status()
    
    issue_url = resp.json()["html_url"]
    print(f"Created issue: {issue_url}")


def main():
    try:
        fragments = fetch_fragments()
        print(f"Loaded {len(fragments)} fragment file(s)")
        
        changed_files = get_changed_files()
        print(f"Detected {len(changed_files)} changed file(s)")
        
        changes = detect_value_changes(fragments, changed_files)
        print(f"Found {len(changes)} fragment value change(s)")
        
        if changes:
            create_issue(changes)
        else:
            print("No fragment changes detected — skipping issue creation")
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
