"""Entry point: load, clean, and preview consolidated sales data."""

from pathlib import Path

from src.cleaner.data_cleaner import clean
from src.loader.excel_loader import load_all_excel_files

RAW_DATA_DIR = Path(__file__).parent / "data" / "raw"


def main():
    print(f"Loading Excel files from: {RAW_DATA_DIR}\n")
    raw = load_all_excel_files(RAW_DATA_DIR)
    print(f"Rows loaded   : {len(raw)}\n")

    df = clean(raw)

    print(f"Files loaded  : {df['source_file'].nunique()}")
    print(f"Total rows    : {len(df)}")
    print(f"Columns       : {list(df.columns)}\n")
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
