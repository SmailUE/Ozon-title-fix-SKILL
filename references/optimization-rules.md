# Russian Ecommerce Title Optimization Rules

These rules are distilled from the training case document `俄语电商商品标题合规优化全集（AI训练结构化案例）.docx` and the CSV dataset `russian_title_compliance.csv`.

## Universal Cleanup Rules

Remove:
- Claims like original/factory/genuine unless the user provided proof.
- Marketing superlatives and sales words: best, hot sale, wholesale, luxury, premium when unsupported, new, popular, direct sales.
- Duplicated synonyms and repeated product nouns.
- Mixed Chinese/English/Russian noise, untranslated English fragments, and obvious mojibake.
- Full-uppercase formatting except real model numbers and acronyms.
- Verb-only or instruction-style phrases such as `Наденьте`, `Вставить`, `Заверните`, `тянуть`, `обрабатывать`.
- Irrelevant scenarios stuffed into the title.
- False or unrelated functions: remove invented uses such as flower drying from shower heads, travel/hotel scenarios from shower filters, or unrelated robot/accessory claims.
- Fragmented ordinary nouns that are not product titles.

Preserve:
- Product type and core noun.
- Material, size, quantity, shape, color, type, and model/part numbers.
- Compatible equipment or vehicle/device model when objective.
- Included accessories and set counts.
- Real use case, but keep it compact and directly relevant.
- Neutral package facts such as `без батареек в комплекте`, set quantities, or included storage bags when present.

Repair:
- Russian cases and prepositions: use `для` when describing intended use or compatibility.
- Word order: product noun first, then material/specification, then use/compatibility.
- Broken phrase fragments into a complete product title when enough product meaning exists.
- English-only simple product words into Russian (`Pendant` -> `Декоративный подвесной элемент`, `The plugG` -> `Штекер`).
- Inappropriate literal translations: replace `поддельный` with `искусственный` for artificial decor.
- CSV rows may be malformed because raw titles contain unquoted commas. When reading training data, treat extra comma-split cells before the final compliant title/explanation as part of the original raw title, not as separate cases.

## Decision Rules For Bad Input

Use `Недействительный товарный заголовок` only when product meaning is not recoverable or the row is not suitable for marketplace listing:
- Only model numbers: `R172272 R172091 R17109790`.
- Single generic word or ordinary noun without product class: `Топливо`, `от`, `Жилье`.
- Pure instruction or action with no recoverable object: `Обрезать`, `Похлопайте по обложке`.
-乱码 or mixed fragments where product category cannot be inferred.
- Generic fragments that cannot be confidently turned into a real SKU title.

If an instruction phrase has a clear implied product, convert it to the object:
- `Наденьте перчатки.` -> `Защитные рабочие перчатки`.
- `Заверните за угол` -> `Угловой фиксирующий элемент`.
- `тянуть линию` -> `Натяжная нить для разметки`.
- `обрабатывать` -> `Обрабатывающая насадка для инструмента`.
- `Вставить тег` -> `Вставной монтажный хомут-тег`.

## Category Term Guidance

### Garden and irrigation
- `Устройство для полива...` -> `Регулируемая капельная система полива...`
- `поливочный пистолет` -> `садовый распылитель`
- Keep size and material: `Металлический садовый распылитель 5 дюймов...`
- `соединитель` for hose connectors; specify `трехходовой`, `быстроразъемный`, `для поливочных шлангов` when present.
- Correct adjective agreement: `Пластиковые сад соединители` -> `Пластиковые садовые соединители`.
- Turn garden decor/support fragments into product nouns: `Металлический кол для цветника`, `Пластиковая подставка для цветов`.

### Automotive, engine, and outdoor power equipment
- Prefer precise part nouns: `детали`, `крышка воздушного фильтра`, `карбюратор двигателя`, `шкив стартера`, `топливный насос`, `глушитель`.
- Preserve part numbers and model compatibility as neutral facts.
- For vague accessories, convert to functional part class, not promotional claims.
- Convert short part names into complete searchable titles: `Карбюратор` -> `Карбюратор двигателя`; `ДЛЯ КРЫЛА` -> `Деталь для крыла техники`.
- For visible/lighting parts, normalize terms such as `рамка для противотуманной фары`, `датчик светового выключателя`, `декоративная накладка для воздухозаборника`.

### Bathroom, plumbing, and kitchen fixtures
- Use standard nouns: `смеситель`, `кран`, `обратный клапан`, `впускной клапан`, `сливная труба`, `сифон`, `насадка-фильтр`, `дозатор мыла`.
- Keep thread/connection sizes such as `G3/8`, `3/4`, `4-6 точек`.
- Remove repeated location stuffing such as bathroom/kitchen/hotel/business trip unless it is directly relevant.
- For shower products, remove mixed English and irrelevant scenario words: `bathing`, `hotel`, `business trip`, `super bathroom`.
- Keep the real product class: `Портативная насадка-фильтр для душа`, `Ручная насадка для душа под давлением`, `Ручная душевая насадка для ванной комнаты`.

### Home storage, furniture, and hardware
- Use concrete part names: `ручка`, `замок`, `петля`, `ролик`, `опора`, `кронштейн`, `защелка`, `ножки стола`.
- Combine scattered related parts into a single coherent product title.
- Keep material, size, quantity: `Замочный механизм 70 мм с медным сердечником, 3 стальных ключа`.
- Normalize all-uppercase hardware: `ПОРТ АДАПТЕРА` -> `Порт адаптера`; `КОЛЬЦА O` -> `Уплотнительное кольцо типа O`; `ГАЙКА` -> `Металлическая гайка`.
- Preserve combinations when they describe one product: `Ручка двери Подлокотник Ящик для хранения` -> `Ручка-подлокотник с ящиком для хранения`.
- Use functional hardware nouns for vague commands: `Заверните за угол` -> `Угловой фиксирующий элемент`.

### Decor and artificial plants
- Use `искусственный`, not `поддельный`.
- Remove mixed English marketing such as `orange fortune fruit`.
- State form and use: `Искусственная композиция... для домашнего декора`, `Длинная гирлянда... для свадебного декора`.
- Replace vague `моделирование` and repeated flower words with concrete decor nouns: `Искусственные цветы...`, `Декоративные фигурки...`, `Декоративный элемент...`.
- Treat pure decor English nouns as translatable when obvious: `Pendant` -> `Декоративный подвесной элемент`.

### Coffee, kitchen tools, and small appliances
- Use compact product class: `Цифровые весы для кофейных зерен`, `Кофейник для холодного заваривания`, `Щетка для чистки кофемолки`, `Круглая крышка для стейка`.
- Preserve material only if useful: `ручка из бука`, `лоток из смолы`.
- For appliances and measuring tools, remove repeated appliance nouns and keep one product class plus use: `Компактный проточный электрический водонагреватель`, `Биметаллический термометр для духовки и барбекю`.

### Ventilation, AC, and filters
- Use terms such as `вентиляционная решетка`, `воздуховод`, `кронштейн кондиционера`, `пылезащитный фильтр`, `HEPA-фильтр`.
- Preserve size and refrigerant models when present: `75 мм`, `R22`, `R410`.

### Electronics, smart home, and appliance parts
- Deduplicate smart-device wording and state application: `Умный термостат для домашних радиаторов отопления`.
- Use professional component terms: `Электромагнитный управляемый клапан`, `Датчик светового выключателя`.
- For e-bike and controller boxes, merge related parts: `Пластиковые корпуса для аккумулятора и контроллера электровелосипеда`.

### Beauty and personal care
- Correct semantic mistranslations: `Прически из волос` is not a product; use `Волосные накладки для создания причесок`.
- Keep objective accessory/use wording and avoid beauty-result claims.

## Example Transformations

| Raw | Standard compliant title | Lesson |
| --- | --- | --- |
| `Пружинные аксессуары для газонокосилки` | `Пружинные детали для газонокосилки` | Use concrete part wording; remove vague accessory phrasing. |
| `Закрытая рамка противотуманной фары` | `Закрытая рамка для противотуманной фары` | Fix Russian preposition and word order. |
| `Умный термостат, умный домашний термостат, умный термостат радиатора` | `Умный термостат для домашних радиаторов отопления` | Remove repetition and state use case. |
| `Биметаллический термометр Термометр для духовки термометр для барбекю` | `Биметаллический термометр для духовки и барбекю` | Merge repeated product nouns and use cases. |
| `The plugG` | `Штекер (деталь двигателя)` | Replace English/noise with Russian product class. |
| `ПОРТ АДАПТЕРА` | `Порт адаптера` | Normalize capitalization. |
| `КОЛЬЦА O` | `Уплотнительное кольцо типа O` | Complete the product function. |
| `от` | `Недействительный товарный заголовок` | Reject meaningless fragments with the fixed invalid-title fallback. |
| `Pendant` | `Декоративный подвесной элемент` | Translate simple English product nouns into Russian. |
| `Насадка для душа под давлением, купание, bathing...` | `Ручная насадка для душа под давлением` | Remove mixed-language and scenario stuffing. |
| `Деревянная шкатулка сосновая...` | `Сосновая шкатулка-коробка для хранения ювелирных изделий` | Keep material and use, remove repeated translated fragments. |
| `Наденьте перчатки.` | `Защитные рабочие перчатки` | Convert a command into product title when object is clear. |
| `Мгновенный электрический водонагреватель, водонагреватель горячей воды, небольшой водонагреватель` | `Компактный проточный электрический водонагреватель` | Merge duplicate appliance nouns and keep objective function. |
| `Металлический поливочный поливочный 5-дюймовый...` | `Металлический садовый распылитель 5 дюймов для полива овощей` | Remove repeated adjectives and wholesale terms; preserve material, size, use. |
| `Карбюратор` | `Карбюратор двигателя` | Add objective application context for search and clarity. |
| `Жилье` | `Недействительный товарный заголовок` | Ordinary noun without product attributes is not listable. |
| `Прически из волос` | `Волосные накладки для создания причесок` | Correct semantic error from result/style to actual product. |
| `ДАТЧИК СВЕТОВОГО ВЫКЛЮЧАТЕЛЯ` | `Датчик светового выключателя` | Normalize all-uppercase formatting while preserving product name. |
| `Пластиковые сад соединители` | `Пластиковые садовые соединители` | Fix Russian adjective agreement. |

## Promotional Title Rules

The promotional title may be longer than the standard title but must stay compliant:
- Add material, size, set count, compatible model, installation context, or objective use.
- Do not add unverifiable benefits such as `лучший`, `профессиональный`, `премиум`, `оригинальный`, `100%`.
- Do not introduce a brand unless the source clearly uses it as compatibility.
- Keep it readable; avoid comma chains longer than 3-4 segments.

Good pattern:
`Сменная крышка воздушного фильтра 595660 для двигателя и садовой техники, защитная деталь корпуса фильтра`

Bad pattern:
`Лучший оригинальный высококачественный фильтр для всех популярных моделей`
