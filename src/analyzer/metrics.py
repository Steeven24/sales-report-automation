from dataclasses import dataclass

import pandas as pd


@dataclass
class AnalysisResult:
    total_revenue: float
    by_product: pd.DataFrame
    by_region: pd.DataFrame
    by_period: pd.DataFrame
    top_products: pd.DataFrame
    monthly_summary: pd.DataFrame


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


def analyze(df: pd.DataFrame) -> AnalysisResult:
    """Run all metrics on the consolidated DataFrame and return an AnalysisResult.

    Metrics computed:
    - Total revenue
    - Revenue and units sold by product
    - Revenue and orders by region
    - Revenue and orders by period (year + month)
    - Top 3 products by revenue
    - Monthly summary (revenue, orders, units sold, avg order value)
    """
    print("Starting analysis...")

    result = AnalysisResult(
        total_revenue=total_revenue(df),
        by_product=revenue_by_product(df),
        by_region=revenue_by_region(df),
        by_period=revenue_by_period(df),
        top_products=top_products(df),
        monthly_summary=monthly_summary(df),
    )

    print(f"  Total revenue     : {result.total_revenue}")
    print(f"  Products analyzed : {len(result.by_product)}")
    print(f"  Regions analyzed  : {len(result.by_region)}")
    print(f"  Months analyzed   : {len(result.by_period)}")
    print("Analysis complete.\n")

    return result
