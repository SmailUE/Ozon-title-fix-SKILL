# russian-title-optimizer

Codex skill for batch-optimizing Russian ecommerce product titles for marketplaces such as Ozon and Wildberries.

## What It Does

- Reads raw product titles from `Sheet1` column A in an Excel workbook.
- Preserves every source row, including duplicates, blank rows, and invalid rows.
- Produces a formatted `.xlsx` output with:
  - `Исходное название`
  - `Стандартный заголовок`
  - `Рекламный заголовок`
- Cleans all-uppercase text, duplicated words, broken spacing, mixed Russian/English/Chinese fragments, and obvious translation artifacts.
- Removes unsafe marketplace wording such as marketing exaggeration, unsupported original/factory/genuine claims, instruction verbs, and irrelevant false functions.
- Marks unrecoverable fragments, generic nouns, and verb-only rows as invalid titles that should not be listed.

## Rule Sources

The current rules were updated from:

- `俄语电商商品标题合规优化全集（AI训练结构化案例）.docx`
- `russian_title_compliance.csv`

The extracted guidance is written into `references/optimization-rules.md`, so the skill does not depend on those original training files after installation.

## File Structure

- `SKILL.md`: Codex execution workflow and output contract.
- `references/optimization-rules.md`: Detailed compliance rules, invalid-title policy, category guidance, and examples.
- `scripts/process_excel.py`: Excel output generation and formatting helper.
- `LICENSE`: MIT license.

## Invalid Title Fallback

When a row has no recoverable product meaning, use:

- Standard title: `Недействительный товарный заголовок`
- Promotional title: `Нельзя использовать для размещения: требуется реальное наименование товара`

Blank source rows stay blank.
