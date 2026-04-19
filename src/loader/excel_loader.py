from pathlib import Path

import pandas as pd


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


def load_excel_file(file_path: str | Path, sheet_name: int | str = 0) -> pd.DataFrame:
    """Load a single Excel file into a DataFrame.

    Adds a 'source_file' column with the file name so the origin
    of each row is traceable after consolidation.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_excel(path, sheet_name=sheet_name, engine="openpyxl")
    df["source_file"] = path.name

    return df


def load_all_excel_files(directory: str, sheet_name: int | str = 0) -> pd.DataFrame:
    """Load all Excel files in a directory and consolidate them into one DataFrame.

    Raises ValueError if no Excel files are found in the directory.
    """
    files = find_excel_files(directory)

    if not files:
        raise ValueError(f"No Excel files found in: {directory}")

    frames = [load_excel_file(file, sheet_name=sheet_name) for file in files]

    return pd.concat(frames, ignore_index=True)
