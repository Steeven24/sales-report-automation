import pandas as pd


def total_revenue(df: pd.DataFrame) -> float:
    """Return the sum of all values in the 'total' column."""
    return round(df["total"].sum(), 2)


def revenue_by_product(df: pd.DataFrame) -> pd.DataFrame:
    """Return total revenue and units sold grouped by product, sorted descending by revenue."""
    return (
        df.groupby("product")
        .agg(revenue=("total", "sum"), units_sold=("quantity", "sum"))
        .round(2)
        .sort_values("revenue", ascending=False)
        .reset_index()
    )


def revenue_by_region(df: pd.DataFrame) -> pd.DataFrame:
    """Return total revenue and number of orders grouped by region, sorted descending by revenue."""
    return (
        df.groupby("region")
        .agg(revenue=("total", "sum"), orders=("total", "count"))
        .round(2)
        .sort_values("revenue", ascending=False)
        .reset_index()
    )
