from pathlib import Path

import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

from src.analyzer.metrics import AnalysisResult

# ── Palette ──────────────────────────────────────────────────────────────────
HEADER_FILL = PatternFill(start_color="2E4057", end_color="2E4057", fill_type="solid")
HEADER_FONT = Font(color="FFFFFF", bold=True)
ACCENT_FILL = PatternFill(start_color="048A81", end_color="048A81", fill_type="solid")
ACCENT_FONT = Font(color="FFFFFF", bold=True, size=11)


def write_dataframe_to_sheet(ws, df: pd.DataFrame, start_row: int = 1) -> None:
    """Write a DataFrame into a worksheet starting at the given row.

    The first row written contains the column headers.
    Values are written as plain Python types so openpyxl can serialize them.
    """
    for col_idx, col_name in enumerate(df.columns, start=1):
        ws.cell(row=start_row, column=col_idx, value=col_name)

    for row_idx, row in enumerate(df.itertuples(index=False), start=start_row + 1):
        for col_idx, value in enumerate(row, start=1):
            if hasattr(value, "item"):
                value = value.item()
            ws.cell(row=row_idx, column=col_idx, value=value)
