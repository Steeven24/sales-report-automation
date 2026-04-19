"""Generate sample Excel sales files for development and testing."""

from pathlib import Path

import pandas as pd

OUTPUT_DIR = Path(__file__).parent.parent / "data" / "raw"

SAMPLES = [
    {
        "filename": "sales_january.xlsx",
        "data": {
            "date": ["2024-01-05", "2024-01-12", "2024-01-20"],
            "product": ["Widget A", "Widget B", "Widget A"],
            "quantity": [10, 5, 8],
            "unit_price": [25.0, 40.0, 25.0],
            "total": [250.0, 200.0, 200.0],
            "region": ["North", "South", "East"],
        },
    },
    {
        "filename": "sales_february.xlsx",
        "data": {
            "date": ["2024-02-03", "2024-02-14", "2024-02-28"],
            "product": ["Widget C", "Widget A", "Widget B"],
            "quantity": [3, 12, 7],
            "unit_price": [60.0, 25.0, 40.0],
            "total": [180.0, 300.0, 280.0],
            "region": ["West", "North", "South"],
        },
    },
    {
        "filename": "sales_march.xlsx",
        "data": {
            "date": ["2024-03-01", "2024-03-15", "2024-03-22"],
            "product": ["Widget B", "Widget C", "Widget A"],
            "quantity": [9, 4, 6],
            "unit_price": [40.0, 60.0, 25.0],
            "total": [360.0, 240.0, 150.0],
            "region": ["East", "West", "North"],
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
