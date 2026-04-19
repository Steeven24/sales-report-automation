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


def monthly_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return a per-month summary with revenue, orders, units sold, and average order value."""
    summary = (
        df.groupby(["year", "month", "month_name"])
        .agg(
            revenue=("total", "sum"),
            orders=("total", "count"),
            units_sold=("quantity", "sum"),
            avg_order_value=("total", "mean"),
        )
        .round(2)
        .sort_values(["year", "month"])
        .reset_index()
    )
    return summary


def top_products(df: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    """Return the top N products by total revenue."""
    return revenue_by_product(df).head(n)


def revenue_by_period(df: pd.DataFrame) -> pd.DataFrame:
    """Return total revenue grouped by year and month, sorted chronologically."""
    return (
        df.groupby(["year", "month", "month_name"])
        .agg(revenue=("total", "sum"), orders=("total", "count"))
        .round(2)
        .sort_values(["year", "month"])
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
