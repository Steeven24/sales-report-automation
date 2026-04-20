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
│   ├── raw/                        # Excel files to process (.xlsx / .xls)
│   └── output/                     # Generated output files
│       ├── consolidated_sales.xlsx
│       ├── consolidated_sales.csv
│       └── sales_report.xlsx       # Final formatted report
├── scripts/
│   └── generate_sample_data.py     # Generates sample files for testing
├── src/
│   ├── loader/
│   │   └── excel_loader.py         # Excel loading and consolidation logic
│   ├── cleaner/
│   │   └── data_cleaner.py         # Data cleaning pipeline
│   ├── merger/
│   │   └── data_merger.py          # Sorting, enrichment, and export pipeline
│   ├── analyzer/
│   │   └── metrics.py              # Sales metrics and analysis
│   └── reporter/
│       └── report_generator.py     # Final Excel report generation
├── tests/
├── main.py                         # Entry point
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
4. Exports the consolidated data to `data/output/` as `.xlsx` and `.csv`
5. Computes sales metrics and prints a full analysis summary
6. Generates the final formatted Excel report at `data/output/sales_report.xlsx`

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
    → merge                     (merger)   →  data/output/consolidated_sales.xlsx / .csv
    → analyze                   (analyzer)
    → generate_report           (reporter) →  data/output/sales_report.xlsx
```

---

## Report sheets

The final `sales_report.xlsx` contains six sheets:

| Sheet | Description |
|---|---|
| `Summary` | KPI block: total revenue, orders, units sold, avg order value, best product and region |
| `By Product` | Revenue and units sold per product, sorted by revenue |
| `By Region` | Revenue and order count per region, sorted by revenue |
| `By Month` | Monthly breakdown: revenue, orders, units sold, avg order value |
| `Top Products` | Top 3 products by revenue |
| `Raw Data` | Full consolidated DataFrame with all columns |

---

## Module reference — `src/loader/excel_loader.py`

| Function | Description |
|---|---|
| `find_excel_files(directory)` | Returns a sorted list of `.xlsx`/`.xls` files found in a directory |
| `load_excel_file(file_path, sheet_name)` | Loads a single Excel file into a `DataFrame`, adding a `source_file` column |
| `load_all_excel_files(directory, sheet_name)` | Combines all Excel files in a directory into one consolidated `DataFrame` |

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

---

## Module reference — `src/merger/data_merger.py`

| Function | Description |
|---|---|
| `sort_by_date(df, date_column)` | Sorts rows chronologically by the date column |
| `add_period_columns(df, date_column)` | Adds `year`, `month`, `month_name`, and `quarter` columns derived from the date |
| `export_to_excel(df, output_path, sheet_name)` | Exports the DataFrame to a single `.xlsx` file |
| `export_to_csv(df, output_path)` | Exports the DataFrame to a single `.csv` file |
| `merge(df)` | Runs the full merging pipeline in order |

---

## Module reference — `src/analyzer/metrics.py`

| Function | Description |
|---|---|
| `total_revenue(df)` | Returns the sum of all values in the `total` column |
| `revenue_by_product(df)` | Revenue and units sold grouped by product, sorted descending |
| `revenue_by_region(df)` | Revenue and order count grouped by region, sorted descending |
| `revenue_by_period(df)` | Revenue and orders grouped by year and month, sorted chronologically |
| `top_products(df, n)` | Returns the top N products by revenue (default: 3) |
| `monthly_summary(df)` | Per-month summary: revenue, orders, units sold, and avg order value |
| `analyze(df)` | Runs all metrics and returns an `AnalysisResult` dataclass |

### AnalysisResult fields

| Field | Type | Description |
|---|---|---|
| `total_revenue` | `float` | Overall revenue across all files |
| `by_product` | `DataFrame` | Revenue and units sold per product |
| `by_region` | `DataFrame` | Revenue and orders per region |
| `by_period` | `DataFrame` | Revenue and orders per month |
| `top_products` | `DataFrame` | Top 3 products by revenue |
| `monthly_summary` | `DataFrame` | Full monthly breakdown |

---

## Module reference — `src/reporter/report_generator.py`

| Function | Description |
|---|---|
| `write_dataframe_to_sheet(ws, df, start_row)` | Writes a DataFrame into a worksheet with headers |
| `auto_fit_columns(ws)` | Adjusts column widths to fit their content |
| `apply_header_style(ws, header_row, col_count)` | Applies bold white text on dark background to header row |
| `create_summary_sheet(ws, result, df)` | Writes the KPI summary block with title and metrics |
| `generate_report(result, df, output_path)` | Creates the final multi-sheet Excel report |

---

## Expected input format

Each Excel file should contain tabular sales data with these columns:

| Column | Type | Description |
|---|---|---|
| `date` | date | Sale date |
| `product` | string | Product name |
| `quantity` | integer | Units sold |
| `unit_price` | float | Price per unit |
| `total` | float | Total sale amount |
| `region` | string | Sales region |

### Output columns (after merging)

| Column | Type | Description |
|---|---|---|
| `source_file` | string | Origin file name |
| `year` | integer | Year extracted from date |
| `month` | integer | Month number (1–12) |
| `month_name` | string | Month name (e.g. January) |
| `quarter` | integer | Quarter number (1–4) |
