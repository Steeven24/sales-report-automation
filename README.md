# Sales Report Automation

Automates the consolidation, cleaning, and analysis of multiple Excel sales files into a single structured report with key metrics and insights.

---

## Requirements

- Python 3.10+
- Dependencies listed in `requirements.txt`

---

## Setup

```bash
# 1. Clone the repository
git clone <repo-url>
cd sales-report-automation

# 2. Create and activate the virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Project structure

```
sales-report-automation/
├── data/
│   ├── raw/                      # Excel files to process (.xlsx / .xls)
│   └── output/                   # Consolidated output files (generated)
│       ├── consolidated_sales.xlsx
│       └── consolidated_sales.csv
├── scripts/
│   └── generate_sample_data.py   # Generates sample files for testing
├── src/
│   ├── loader/
│   │   └── excel_loader.py       # Excel loading and consolidation logic
│   ├── cleaner/
│   │   └── data_cleaner.py       # Data cleaning pipeline
│   └── merger/
│       └── data_merger.py        # Sorting, enrichment, and export pipeline
├── tests/
├── main.py                       # Entry point
└── requirements.txt
```

---

## Usage

### Run the full pipeline

```bash
python main.py
```

Place your `.xlsx` or `.xls` files inside `data/raw/` and run the command above. The pipeline:

1. Loads all Excel files from `data/raw/`
2. Cleans the data (removes nulls, duplicates, invalid values, normalizes text)
3. Sorts rows chronologically and adds period columns (year, month, quarter)
4. Exports the consolidated result to `data/output/` as `.xlsx` and `.csv`

### Generate sample data (for testing)

```bash
python scripts/generate_sample_data.py
```

Creates three sample Excel files in `data/raw/` covering January, February, and March 2024.
The files include intentionally dirty records (nulls, duplicates, bad dates, invalid values) to exercise the cleaning pipeline.

---

## Full pipeline

```
data/raw/*.xlsx
    → load_all_excel_files      (loader)
    → clean                     (cleaner)
    → merge                     (merger)
    → data/output/consolidated_sales.xlsx
    → data/output/consolidated_sales.csv
```

---

## Module reference — `src/loader/excel_loader.py`

| Function | Description |
|---|---|
| `find_excel_files(directory)` | Returns a sorted list of `.xlsx`/`.xls` files found in a directory |
| `load_excel_file(file_path, sheet_name)` | Loads a single Excel file into a `DataFrame`, adding a `source_file` column |
| `load_all_excel_files(directory, sheet_name)` | Combines all Excel files in a directory into one consolidated `DataFrame` |

The `source_file` column is added automatically so each row stays traceable to its origin file after consolidation.

---

## Module reference — `src/cleaner/data_cleaner.py`

| Function | Description |
|---|---|
| `drop_empty_rows(df, required_columns)` | Removes rows with null values in any required column |
| `drop_duplicates(df, subset)` | Removes duplicate rows, keeping the first occurrence |
| `normalize_text_columns(df, columns)` | Strips whitespace and applies title case to string columns |
| `parse_dates(df, date_column)` | Converts a date column to `datetime`, dropping unparseable rows |
| `cast_numeric_columns(df, columns)` | Coerces columns to `float`, dropping rows where conversion fails |
| `remove_invalid_values(df, positive_columns)` | Drops rows with zero or negative values in numeric columns |
| `clean(df)` | Runs the full cleaning pipeline in order |

### Cleaning pipeline order

```
raw DataFrame
    → drop_empty_rows
    → drop_duplicates
    → normalize_text_columns
    → parse_dates
    → cast_numeric_columns
    → remove_invalid_values
    → clean DataFrame
```

---

## Module reference — `src/merger/data_merger.py`

| Function | Description |
|---|---|
| `sort_by_date(df, date_column)` | Sorts rows chronologically by the date column |
| `add_period_columns(df, date_column)` | Adds `year`, `month`, `month_name`, and `quarter` columns derived from the date |
| `export_to_excel(df, output_path, sheet_name)` | Exports the DataFrame to a single `.xlsx` file |
| `export_to_csv(df, output_path)` | Exports the DataFrame to a single `.csv` file |
| `merge(df)` | Runs the full merging pipeline in order |

### Merging pipeline order

```
clean DataFrame
    → sort_by_date
    → add_period_columns
    → export_to_excel   →  data/output/consolidated_sales.xlsx
    → export_to_csv     →  data/output/consolidated_sales.csv
    → merged DataFrame
```

---

## Expected input format

Each Excel file should contain tabular sales data. The sample files include these columns:

| Column | Type | Description |
|---|---|---|
| `date` | date | Sale date |
| `product` | string | Product name |
| `quantity` | integer | Units sold |
| `unit_price` | float | Price per unit |
| `total` | float | Total sale amount |
| `region` | string | Sales region |

### Output columns (after merging)

The consolidated output includes all input columns plus the period columns added during merging:

| Column | Type | Description |
|---|---|---|
| `source_file` | string | Origin file name |
| `year` | integer | Year extracted from date |
| `month` | integer | Month number (1–12) |
| `month_name` | string | Month name (e.g. January) |
| `quarter` | integer | Quarter number (1–4) |
