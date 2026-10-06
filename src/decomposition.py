"""
# Phase 2-3: the math, phase detection
"""

import numpy as np
import pandas as pd


def add_decomposition(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["PE"] = df["P"] / df["E"]
    df["ret_P"] = np.log(df["P"]).diff()
    df["ret_E"] = np.log(df["E"]).diff()
    df["ret_PE"] = np.log(df["PE"]).diff()
    return df


def decade_summary(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=["ret_P"]).copy()
    df["decade"] = (df["Date"].dt.year // 10) * 10
    return df.groupby("decade")[["ret_P", "ret_E", "ret_PE"]].sum()