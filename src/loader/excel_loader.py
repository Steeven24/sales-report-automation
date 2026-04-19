import os
from pathlib import Path


def find_excel_files(directory: str) -> list[Path]:
    """Return all .xlsx and .xls files found inside a directory."""
    folder = Path(directory)

    if not folder.exists():
        raise FileNotFoundError(f"Directory not found: {directory}")

    if not folder.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {directory}")

    excel_extensions = {".xlsx", ".xls"}
    return [
        file
        for file in sorted(folder.iterdir())
        if file.suffix.lower() in excel_extensions
    ]
