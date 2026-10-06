"""
# Phase 1: fetch + clean
"""

import pandas as pd


def load_shiller_data(filepath: str) -> pd.DataFrame:
    """Load and clean Shiller's monthly S&P 500 dataset (Date, P, D, E, CPI)."""
    df = pd.read_excel(filepath, sheet_name="Data", skiprows=7)
    df = df[["Date", "P", "D", "E", "CPI"]]
    df = df.dropna(subset=["E"])
    date_str = df["Date"].map(lambda x: f"{x:.2f}")
    df["Date"] = pd.to_datetime(date_str.str.slice(0, 4) + "-" + date_str.str.slice(5, 7) + "-01")
    df[["P", "CPI"]] = df[["P", "CPI"]].astype(float)
    df = df.sort_values("Date").reset_index(drop=True)
    return df