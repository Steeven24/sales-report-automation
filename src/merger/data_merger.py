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
