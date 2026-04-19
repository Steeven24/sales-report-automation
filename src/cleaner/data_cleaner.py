import pandas as pd


def drop_empty_rows(df: pd.DataFrame, required_columns: list[str]) -> pd.DataFrame:
    """Remove rows that have null values in any of the required columns."""
    before = len(df)
    df = df.dropna(subset=required_columns)
    dropped = before - len(df)

    if dropped:
        print(f"  [drop_empty_rows] Removed {dropped} row(s) with null values.")

    return df.reset_index(drop=True)
