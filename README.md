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
│   └── raw/                      # Excel files to process (.xlsx / .xls)
├── scripts/
│   └── generate_sample_data.py   # Generates sample files for testing
├── src/
│   ├── loader/
│   │   └── excel_loader.py       # Excel loading and consolidation logic
│   └── cleaner/
│       └── data_cleaner.py       # Data cleaning pipeline
├── tests/
├── main.py                       # Entry point
└── requirements.txt
```

---

## Usage

### Load, clean, and preview all sales files

```bash
python main.py
```

Place your `.xlsx` or `.xls` files inside `data/raw/` and run the command above.
The pipeline loads all files, cleans the data, and prints a preview of the consolidated result.

### Generate sample data (for testing)

```bash
python scripts/generate_sample_data.py
```

Creates three sample Excel files in `data/raw/` covering January, February, and March 2024.
The files include intentionally dirty records (nulls, duplicates, bad dates, invalid values) to exercise the cleaning pipeline.

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
| `clean(df)` | Runs the full pipeline in order — the main entry point for cleaning |

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
