import pandas as pd


def sort_by_date(df: pd.DataFrame, date_column: str = "date") -> pd.DataFrame:
    """Sort the DataFrame chronologically by the date column."""
    if date_column not in df.columns:
        raise KeyError(f"Column '{date_column}' not found in DataFrame.")

    return df.sort_values(by=date_column).reset_index(drop=True)
