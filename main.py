"""Entry point: load, clean, merge, analyze, and generate the final sales report."""

from pathlib import Path

from src.analyzer.metrics import analyze
from src.cleaner.data_cleaner import clean
from src.loader.excel_loader import load_all_excel_files
from src.merger.data_merger import merge
from src.reporter.report_generator import generate_report

RAW_DATA_DIR = Path(__file__).parent / "data" / "raw"


def main():
    print(f"Loading Excel files from: {RAW_DATA_DIR}\n")
    raw = load_all_excel_files(RAW_DATA_DIR)
    print(f"Rows loaded   : {len(raw)}\n")

    cleaned = clean(raw)
    merged = merge(cleaned)
    result = analyze(merged)

    print("=" * 50)
    print(f"Total revenue    : ${result.total_revenue:,.2f}")
    print("=" * 50)

    print("\nRevenue by product:")
    print(result.by_product.to_string(index=False))

    print("\nRevenue by region:")
    print(result.by_region.to_string(index=False))

    print("\nMonthly summary:")
    print(result.monthly_summary.to_string(index=False))

    print("\nTop products:")
    print(result.top_products.to_string(index=False))

    print()
    report_path = generate_report(result, merged)
    print(f"\nReport ready: {report_path.resolve()}")


if __name__ == "__main__":
    main()
