"""Entry point: load all Excel sales files and print a summary."""

from pathlib import Path

from src.loader.excel_loader import load_all_excel_files

RAW_DATA_DIR = Path(__file__).parent / "data" / "raw"


def main():
    print(f"Loading Excel files from: {RAW_DATA_DIR}\n")

    df = load_all_excel_files(RAW_DATA_DIR)

    print(f"Files loaded  : {df['source_file'].nunique()}")
    print(f"Total rows    : {len(df)}")
    print(f"Columns       : {list(df.columns)}\n")
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
