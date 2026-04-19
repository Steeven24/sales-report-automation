"""Generate sample Excel sales files for development and testing.

Includes intentionally dirty data to exercise the cleaning pipeline:
- Null values in required columns
- Duplicate rows
- Inconsistent text casing and extra whitespace
- Non-numeric values in numeric columns
- Zero and negative quantities/prices
- Unparseable date strings
"""

from pathlib import Path

import pandas as pd

OUTPUT_DIR = Path(__file__).parent.parent / "data" / "raw"

SAMPLES = [
    {
        "filename": "sales_january.xlsx",
        "data": {
            "date": ["2024-01-05", "2024-01-12", "2024-01-20", "2024-01-20", "NOT A DATE"],
            "product": ["Widget A", "  widget b  ", "Widget A", "Widget A", "Widget C"],
            "quantity": [10, 5, 8, 8, -3],
            "unit_price": [25.0, 40.0, 25.0, 25.0, 60.0],
            "total": [250.0, 200.0, 200.0, 200.0, -180.0],
            "region": ["North", "SOUTH", "East", "East", "West"],
        },
    },
    {
        "filename": "sales_february.xlsx",
        "data": {
            "date": ["2024-02-03", "2024-02-14", "2024-02-28", "2024-02-10", "2024-02-20"],
            "product": ["Widget C", "Widget A", "Widget B", None, "widget a"],
            "quantity": [3, 12, 7, 5, "N/A"],
            "unit_price": [60.0, 25.0, 40.0, 25.0, 25.0],
            "total": [180.0, 300.0, 280.0, None, 100.0],
            "region": ["West", "north", "South", "East", "  NORTH  "],
        },
    },
    {
        "filename": "sales_march.xlsx",
        "data": {
            "date": ["2024-03-01", "2024-03-15", "2024-03-22", "2024-03-10"],
            "product": ["Widget B", "Widget C", "Widget A", "WIDGET B"],
            "quantity": [9, 4, 6, 0],
            "unit_price": [40.0, 60.0, 25.0, 40.0],
            "total": [360.0, 240.0, 150.0, 0.0],
            "region": ["East", "west", "North", "South"],
        },
    },
]


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for sample in SAMPLES:
        file_path = OUTPUT_DIR / sample["filename"]
        df = pd.DataFrame(sample["data"])
        df.to_excel(file_path, index=False)
        print(f"Created: {file_path}")


if __name__ == "__main__":
    main()
