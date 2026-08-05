---
name: russian-title-optimizer
description: Batch-optimize Russian ecommerce product titles from Excel files for marketplaces such as Ozon and Wildberries. Use when the user provides a spreadsheet of raw Russian, mixed-language, mistranslated, duplicated, or messy product titles and wants a formatted .xlsx output with original titles, compliant concise standard titles, and longer traffic-oriented titles.
---

# Russian Title Optimizer

Optimize raw ecommerce product titles in `Sheet1` column A of an Excel workbook.

## Output Contract

- Preserve every source row exactly: row order, duplicates, blank rows, and invalid rows must not be skipped.
- Output a downloadable `.xlsx` with three columns:
  1. `Исходное название`
  2. `Стандартный заголовок`
  3. `Рекламный заголовок`
- Format the output workbook with a blue header row, bold white header text, thin borders, frozen first row, wrapped text, suitable column widths, and pure white content rows. Do not use zebra striping.
- For blank source rows, leave both optimized title columns blank.
- For repeated source titles, reuse the same optimized pair consistently.

## Core Workflow

1. Read all values from `Sheet1` column A.
2. Read `references/optimization-rules.md` before generating titles.
3. Clean each nonblank title into a concise compliant Russian standard title.
4. Create a longer promotional title only from objective product attributes: product type, material, size/model, use case, compatibility, set quantity, and included accessories.
5. Generate the formatted workbook with `scripts/process_excel.py` or equivalent logic.
6. Verify the output opens and that source row count, filled-row count, blank-row count, and optimized-row count match expectations.

## Title Policy

- Prefer objective, marketplace-safe Russian. Avoid exaggerated claims, sales language, brand/original-factory claims, and unsupported compatibility.
- Remove repeated nouns, mixed-language fragments, translation artifacts, meaningless words, raw commands, and irrelevant scenario stuffing.
- Normalize Russian grammar, word order, case endings, capitalization, units, and product terminology.
- Preserve concrete product facts: material, shape, size, quantity, model numbers, compatible equipment, intended use, and included accessories.
- Keep brand/model identifiers only when they appear to be neutral compatibility or part numbers. Remove or soften identifiers that look like infringement-prone brand promotion.
- If a row is only a verb, generic noun, model numbers without product class,乱码, or otherwise has no recoverable product meaning, mark it as invalid and not suitable for listing:
  - Standard: `Недействительный товарный заголовок`
  - Promotional: `Нельзя использовать для размещения: требуется реальное наименование товара`

## Standard Vs Promotional Titles

- Standard title: short, search-weighted, product-first. Pattern: `Product + key attribute/use`.
- Promotional title: longer but still factual. Pattern: `Product + material/spec/model + use case/compatibility + objective benefit/accessory`.
- Do not invent capabilities. If the source is ambiguous, write a conservative category title or fallback.
