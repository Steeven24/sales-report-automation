from pathlib import Path

import pandas as pd


def sort_by_date(df: pd.DataFrame, date_column: str = "date") -> pd.DataFrame:
    """Sort the DataFrame chronologically by the date column."""
    if date_column not in df.columns:
        raise KeyError(f"Column '{date_column}' not found in DataFrame.")

    return df.sort_values(by=date_column).reset_index(drop=True)


def add_period_columns(df: pd.DataFrame, date_column: str = "date") -> pd.DataFrame:
    """Derive year, month, month_name, and quarter columns from the date column.

    These columns make it easy to group and filter data by time period
    without parsing dates repeatedly downstream.
    """
    if date_column not in df.columns:
        raise KeyError(f"Column '{date_column}' not found in DataFrame.")

    df = df.copy()
    df["year"] = df[date_column].dt.year
    df["month"] = df[date_column].dt.month
    df["month_name"] = df[date_column].dt.strftime("%B")
    df["quarter"] = df[date_column].dt.quarter

    return df


def export_to_excel(df: pd.DataFrame, output_path: str | Path, sheet_name: str = "Sales") -> Path:
    """Export the DataFrame to a single Excel file.

    Creates any missing parent directories automatically.
    Returns the resolved output path.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with pd.ExcelWriter(path, engine="openpyxl", datetime_format="YYYY-MM-DD") as writer:
        df.to_excel(writer, index=False, sheet_name=sheet_name)

    print(f"  [export_to_excel] Saved {len(df)} row(s) to {path}")

    return path


def export_to_csv(df: pd.DataFrame, output_path: str | Path) -> Path:
    """Export the DataFrame to a single CSV file.

    Creates any missing parent directories automatically.
    Returns the resolved output path.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(path, index=False, encoding="utf-8")
    print(f"  [export_to_csv] Saved {len(df)} row(s) to {path}")

    return path


OUTPUT_EXCEL = Path("data/output/consolidated_sales.xlsx")
OUTPUT_CSV = Path("data/output/consolidated_sales.csv")


def merge(df: pd.DataFrame) -> pd.DataFrame:
    """Run the full merging pipeline on a cleaned sales DataFrame.

    Steps applied in order:
    1. Sort rows chronologically by date
    2. Add period columns: year, month, month_name, quarter
    3. Export to a single Excel file
    4. Export to a single CSV file
    """
    print("Starting data merging pipeline...")

    df = sort_by_date(df)
    df = add_period_columns(df)
    export_to_excel(df, OUTPUT_EXCEL)
    export_to_csv(df, OUTPUT_CSV)

    print(f"Merging complete. Consolidated file has {len(df)} row(s).\n")
    return df
