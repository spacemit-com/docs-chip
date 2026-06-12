# Doc Review Agent

An automated documentation reviewer for the `docs-chip` repository. It runs on every pull request that touches Markdown files under `en/` or `zh/`, posts inline comments directly on the diff, and leaves a summary. A human makes the final merge decision.

---

## How It Works

```
PR opened / updated
       │
       ▼
GitHub Actions triggers doc-review.yml
       │
       ▼
agent.py runs two passes:
  1. Rule-based checks  (fast, deterministic)
  2. LLM-assisted review (optional, requires OPENAI_API_KEY)
       │
       ▼
Inline comments posted on specific lines
Summary comment posted at PR level
       │
       ▼
Human reviews comments → modifies, ignores, or merges
```

The agent only **comments** — it never approves, requests changes, or blocks merge.

---

## File Structure

```
.github/
├── workflows/
│   └── doc-review.yml          # GitHub Actions trigger
└── doc-review-agent/
    ├── agent.py                # Main agent script
    ├── config.yml              # Check toggles and thresholds
    └── system_prompt.md        # LLM style guide and output rules
```

---

## Checks

| Check | Scope | Severity |
|-------|-------|----------|
| YAML frontmatter exists and has required fields | `en/`, `zh/` | Warning |
| Heading levels are not skipped | `en/`, `zh/` | Warning |
| No `TBD` / `TODO` / `FIXME` placeholders | `en/`, `zh/` | Warning |
| Internal Markdown links resolve to existing files | `en/`, `zh/` | Error |
| Images referenced in `![](path)` exist in `static/` | `en/`, `zh/` | Error |
| Code blocks have a language identifier | `en/`, `zh/` | Suggestion |
| Bilingual counterpart file exists (`en/` ↔ `zh/`) | both | Warning |
| Chinese punctuation used in `zh/` files | `zh/` only | Suggestion |
| LLM content review (technical accuracy, style) | `en/`, `zh/` | varies |

All checks can be toggled individually in `config.yml`.

---

## Setup

### 1. Secrets and Variables

In your GitHub repository, go to **Settings → Secrets and variables → Actions** and add:

| Name | Type | Description |
|------|------|-------------|
| `OPENAI_API_KEY` | Secret | LLM API key. Leave empty to skip LLM review. |
| `OPENAI_BASE_URL` | Secret | Optional. Custom endpoint (e.g., Azure OpenAI). Defaults to `https://api.openai.com/v1`. |
| `OPENAI_MODEL` | Variable | Optional. Model name. Defaults to `gpt-4o`. |

`GITHUB_TOKEN` is provided automatically by GitHub Actions — no setup needed.

### 2. Enable the Workflow

The workflow file is already at `.github/workflows/doc-review.yml`. Push it to `main` and it activates automatically on the next PR.

### 3. Configure Checks

Edit `.github/doc-review-agent/config.yml` to enable/disable individual checks or adjust thresholds.

---

## Output Format

### Inline Comment (English file)

> `[Warning]` Figure 3 is referenced in the text but not present in the `static/` directory. Add the missing image or update the reference.
>
> `<!-- bot:doc-review -->`

### Inline Comment (Chinese file)

> `[错误]` 未找到对应的英文文档：`en/key_stone/k1/k1_docs/k1_ds.md`。请创建对应文件或更新语言索引。
>
> `<!-- bot:doc-review -->`

### PR Summary

```
## 📋 Doc Review Summary

| Severity   | Count |
|------------|-------|
| Error      | 2     |
| Warning    | 3     |
| Suggestion | 1     |

> Errors indicate missing or incorrect information that should be addressed before merge.
> Warnings and suggestions are advisory — human reviewer makes the final call.
```

---

## Dismissing False Positives

All bot comments contain the tag `<!-- bot:doc-review -->`. To dismiss:

- Click **Resolve conversation** on any comment you disagree with.
- The agent will not re-post resolved comments on re-runs.

To permanently suppress a rule, set it to `enabled: false` in `config.yml`.

---

## Local Testing

```bash
pip install requests pyyaml

export GITHUB_TOKEN="ghp_..."
export GITHUB_REPOSITORY="spacemit-com/docs-chip"
export PR_NUMBER="42"
export OPENAI_API_KEY="sk-..."   # optional
export GITHUB_WORKSPACE="."

python .github/doc-review-agent/agent.py
```
