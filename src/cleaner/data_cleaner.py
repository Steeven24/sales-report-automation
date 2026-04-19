import pandas as pd


def drop_empty_rows(df: pd.DataFrame, required_columns: list[str]) -> pd.DataFrame:
    """Remove rows that have null values in any of the required columns."""
    before = len(df)
    df = df.dropna(subset=required_columns)
    dropped = before - len(df)

    if dropped:
        print(f"  [drop_empty_rows] Removed {dropped} row(s) with null values.")

    return df.reset_index(drop=True)


def normalize_text_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Strip whitespace and apply title case to the given string columns."""
    for col in columns:
        if col not in df.columns:
            raise KeyError(f"Column '{col}' not found in DataFrame.")
        df[col] = df[col].astype(str).str.strip().str.title()

    return df


def cast_numeric_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Coerce the given columns to float, dropping rows where conversion fails."""
    for col in columns:
        if col not in df.columns:
            raise KeyError(f"Column '{col}' not found in DataFrame.")

        before = len(df)
        df[col] = pd.to_numeric(df[col], errors="coerce")

        invalid = df[col].isna().sum()
        if invalid:
            df = df.dropna(subset=[col])
            print(f"  [cast_numeric_columns] Removed {before - len(df)} row(s) with non-numeric '{col}'.")

    return df.reset_index(drop=True)


def parse_dates(df: pd.DataFrame, date_column: str) -> pd.DataFrame:
    """Convert a date column from string to datetime, dropping unparseable rows."""
    if date_column not in df.columns:
        raise KeyError(f"Column '{date_column}' not found in DataFrame.")

    before = len(df)
    df[date_column] = pd.to_datetime(df[date_column], errors="coerce")

    invalid = df[date_column].isna().sum()
    if invalid:
        df = df.dropna(subset=[date_column])
        print(f"  [parse_dates] Removed {invalid} row(s) with unparseable dates.")

    dropped = before - len(df)
    if dropped == 0:
        pass  # all dates parsed successfully

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
