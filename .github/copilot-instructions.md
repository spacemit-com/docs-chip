# GitHub Copilot Instructions — docs-chip

This repository contains bilingual (English + Chinese) technical documentation for SpacemiT SoC products: **K1, K3** (key_stone family) and **P1, P1S** (power_stone family). Docs cover datasheets, hardware design guides, user manuals, SDK guides, and FAQs.

---

## Repository Layout

```
en/   # English docs
zh/   # Chinese docs (mirrors en/ structure exactly)
  key_stone/
    k1/
      k1_docs/        # Datasheet, product brief, user manual
        k1_usermanual/ # Chapter-per-file structure
        static/        # Images for k1_docs
      k1_hw/          # Hardware design guide, AVL, FAQs, resources
        static/
      k1_sw/          # SDK user guide, SW FAQ
        static/
    k3/  (same pattern)
  power_stone/
    p1/   p1s/  (same pattern)
.github/
  workflows/doc-review.yml          # CI: runs on every PR touching en/**/*.md or zh/**/*.md
  doc-review-agent/
    agent.py          # Rule-based + LLM review script
    config.yml        # Check toggles and thresholds
    system_prompt.md  # LLM reviewer style guide
```

---

## Frontmatter Format

Files in this repo do **not** use YAML `---` blocks. The frontmatter is a single bare line:

```
sidebar_position: 2

# Section Title
```

Never generate `---` YAML frontmatter blocks. Always use the bare `sidebar_position: N` format.

---

## Copilot Tasks in This Repo

Use the appropriate task pattern below when the user asks for help.

### 1. Write or Edit Documentation

- Match the style of existing files: concise technical prose, bullet lists for features, tables for specs and revision history.
- `en/` files: English only. `zh/` files: Chinese only. Never mix languages within a file.
- Always include a `sidebar_position` frontmatter field (integer) at the top of the file, matching the position of neighboring files in the same directory.
- Preserve existing heading hierarchy (`#` → `##` → `###`). Do not skip levels.
- Use proper units: voltage in V, current in mA/A, frequency in MHz/GHz, temperature in °C.
- In `zh/` files: keep technical acronyms in English (SoC, PCIe, DDR4, LPDDR4X, GPIO, UART, I²C, SPI, EVB, BOM, TDP); use Chinese for surrounding prose.
- Images go in the `static/` subfolder of the same section. Reference them as `![](./static/filename.ext)` or `![](static/filename.ext)`.
- Do not add `TBD`, `TODO`, or `FIXME` placeholders — the CI will flag them.
- Code blocks must always have a language identifier (e.g., ` ```bash `, ` ```c `, ` ```yaml `).

### 2. Translate Between English and Chinese

When translating a file from `en/` → `zh/` (or vice versa):
- Preserve the exact same `sidebar_position` value.
- Preserve the exact same heading structure and order.
- Preserve all Markdown formatting: tables, code blocks, bold/italic, links.
- Keep all links identical — do not translate URL paths or anchor names.
- Image references stay the same (images are shared via the `static/` folder convention).
- Translate prose naturally; do not translate technical acronyms (see §1 above).
- PDF download links: replace `_en.pdf` with `_zh.pdf` (or vice versa) in the URL.

### 3. Add a New Chip or Document Section

When adding a new chip (e.g., `k5`) or a new section:
- Mirror the structure in **both** `en/` and `zh/` simultaneously.
- Create an `index.md` in every new directory.
- Add a `banner.txt` at the chip root level (matching the pattern in existing chips).
- Place images in a `static/` subfolder inside the relevant section.
- Update parent `index.md` files to link to the new section.

### 4. Check Bilingual Sync

When asked whether `en/` and `zh/` are in sync:
- Compare directory trees of both sides.
- List files present in `en/` but missing in `zh/`, and vice versa.
- Compare heading counts in paired files to detect content divergence.
- Report results clearly; do not auto-modify files unless the user asks.

### 5. Review a Document (pre-PR check)

Before the user opens a PR, they may ask for a review. Apply the same checks the CI runs:
- YAML frontmatter has `sidebar_position`.
- No heading levels are skipped.
- No `TBD` / `TODO` / `FIXME` in content.
- All internal Markdown links resolve to existing files.
- All images referenced with `![](...)` exist in the corresponding `static/` folder.
- Code blocks have language identifiers.
- The bilingual counterpart file exists.
- In `zh/` files: Chinese punctuation is used (「，。、：；」 not `,.:;`).

Report issues using the same format as the CI agent:
- English files: `` `[Error]` `` / `` `[Warning]` `` / `` `[Suggestion]` ``
- Chinese files: `` `[错误]` `` / `` `[警告]` `` / `` `[建议]` ``

---

## Terminology Reference

| English | Chinese |
|---|---|
| Datasheet | 数据手册 |
| User Manual | 用户手册 |
| Hardware Design Guide | 硬件设计指南 |
| SDK User Guide | SDK 用户指南 |
| Product Brief | 产品简介 |
| Evaluation Board (EVB) | 评估板 |
| power rail | 电源轨 |
| boot sequence | 启动序列 |
| register map | 寄存器映射 |
| memory map | 内存映射 |
| thermal dissipation | 散热方案 |
| signal integrity | 信号完整性 |
| schematic | 原理图 |
| layout guideline | 布局布线规范 |
| interrupt controller | 中断控制器 |

---

## CI / Workflow Notes

- The `doc-review.yml` workflow triggers on PRs that touch `en/**/*.md` or `zh/**/*.md`.
- It runs `agent.py` which does rule-based checks + optional LLM review (requires `OPENAI_API_KEY` secret).
- The agent only posts comments — it never blocks merge.
- `index.md` files are excluded from review by `config.yml`.
- To change check behavior, edit `.github/doc-review-agent/config.yml`.

---

## Prompt Templates for Common Tasks

When the user's request matches one of these patterns, follow the template exactly.

### Translate a file
> "把 `en/key_stone/k1/k1_hw/k1_hw_faq.md` 翻译成中文"

1. Read the source file.
2. Identify `sidebar_position` value — keep it identical.
3. Translate all prose to Chinese; keep all acronyms in English.
4. Replace PDF link suffix: `_en.pdf` → `_zh.pdf`.
5. Write the translated file to the mirrored path under `zh/`.
6. Report: file written, any links that could not be verified.

### Review a file before PR
> "帮我 review 一下 `zh/key_stone/k1/k1_docs/k1_ds.md`"

Run all checks from §5 above. Output findings grouped by severity:
- `[错误]` items first
- `[警告]` items second
- `[建议]` items last

If no issues found, say so explicitly.

### Check bilingual sync
> "en 和 zh 有哪些文件不同步？"

1. List all `.md` files under `en/` (excluding `index.md`).
2. For each, check if the mirrored path under `zh/` exists.
3. For existing pairs, compare `##` heading count — flag if difference > 2.
4. Output a table: `| en/ file | zh/ counterpart | Status |`

### Add a new chip section
> "帮我新建 k5 的文档目录"

1. Mirror the structure of an existing chip (e.g., k1) in both `en/` and `zh/`.
2. Create: `index.md`, `banner.txt`, `k5_docs/index.md`, `k5_hw/index.md`, `k5_sw/index.md`, and `static/` dirs.
3. Update parent `key_stone/index.md` in both languages.
4. Set `sidebar_position` values to follow the existing sequence.
