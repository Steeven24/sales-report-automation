import pandas as pd


def drop_empty_rows(df: pd.DataFrame, required_columns: list[str]) -> pd.DataFrame:
    """Remove rows that have null values in any of the required columns."""
    before = len(df)
    df = df.dropna(subset=required_columns)
    dropped = before - len(df)

    if dropped:
        print(f"  [drop_empty_rows] Removed {dropped} row(s) with null values.")

    return df.reset_index(drop=True)


def drop_duplicates(df: pd.DataFrame, subset: list[str] | None = None) -> pd.DataFrame:
    """Remove duplicate rows.

    If subset is provided, duplicates are checked only on those columns.
    The first occurrence is kept.
    """
    before = len(df)
    df = df.drop_duplicates(subset=subset, keep="first")
    dropped = before - len(df)

    if dropped:
        print(f"  [drop_duplicates] Removed {dropped} duplicate row(s).")

    return df.reset_index(drop=True)
