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

def add_cape(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    adj = df["CPI"].iloc[-1] / df["CPI"]
    df["P_real"] = df["P"] * adj
    df["E_real"] = df["E"] * adj
    df["CAPE"] = df["P_real"] / df["E_real"].rolling(120).mean()
    return df

def add_rolling_regime(df: pd.DataFrame, window: int = 120) -> pd.DataFrame:
    df = df.copy()
    for c in ["ret_P", "ret_E", "ret_PE"]:
        df[f"{c}_roll"] = df[c].rolling(window).sum()
    df["regime"] = np.where(
        df["ret_PE_roll"].abs() > df["ret_E_roll"].abs(), "multiple-driven", "earnings-driven"
    )
    df.loc[df["ret_P_roll"].isna(), "regime"] = None
    return df