import pandas as pd


def total_revenue(df: pd.DataFrame) -> float:
    """Return the sum of all values in the 'total' column."""
    return round(df["total"].sum(), 2)
