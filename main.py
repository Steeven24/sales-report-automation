"""Entry point: load, clean, merge, and export consolidated sales data."""

from pathlib import Path

from src.cleaner.data_cleaner import clean
from src.loader.excel_loader import load_all_excel_files
from src.merger.data_merger import merge

RAW_DATA_DIR = Path(__file__).parent / "data" / "raw"


def main():
    print(f"Loading Excel files from: {RAW_DATA_DIR}\n")
    raw = load_all_excel_files(RAW_DATA_DIR)
    print(f"Rows loaded   : {len(raw)}\n")

    cleaned = clean(raw)
    merged = merge(cleaned)

    print(f"Files processed : {merged['source_file'].nunique()}")
    print(f"Total rows      : {len(merged)}")
    print(f"Columns         : {list(merged.columns)}\n")
    print(merged.to_string(index=False))


if __name__ == "__main__":
    main()
