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
│   └── raw/                  # Excel files to process (.xlsx / .xls)
├── scripts/
│   └── generate_sample_data.py   # Generates sample files for testing
├── src/
│   └── loader/
│       └── excel_loader.py   # Excel loading and consolidation logic
├── tests/
├── main.py                   # Entry point
└── requirements.txt
```

---

## Usage

### Load and preview all sales files

```bash
python main.py
```

Place your `.xlsx` or `.xls` files inside `data/raw/` and run the command above.
The output shows the total rows loaded, the columns present, and a preview of the consolidated data.

### Generate sample data (for testing)

```bash
python scripts/generate_sample_data.py
```

Creates three sample Excel files in `data/raw/` covering January, February, and March 2024.

---

## Module reference — `src/loader/excel_loader.py`

| Function | Description |
|---|---|
| `find_excel_files(directory)` | Returns a sorted list of `.xlsx`/`.xls` files found in a directory |
| `load_excel_file(file_path, sheet_name)` | Loads a single Excel file into a `DataFrame`, adding a `source_file` column |
| `load_all_excel_files(directory, sheet_name)` | Combines all Excel files in a directory into one consolidated `DataFrame` |

The `source_file` column is added automatically so each row stays traceable to its origin file after consolidation.

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
