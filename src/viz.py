"""
# Phase 4: chart functions
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot_decade_decomposition(summary: pd.DataFrame, path: str) -> None:
    fig, ax = plt.subplots(figsize=(12, 6))
    x = np.arange(len(summary))
    w = 0.38
    ax.bar(x - w / 2, summary["ret_E"], w, label="Earnings growth", color="#2a6f97")
    ax.bar(x + w / 2, summary["ret_PE"], w, label="P/E multiple change", color="#e07a5f")
    ax.scatter(x, summary["ret_P"], color="black", zorder=3, label="Total price return")
    ax.axhline(0, color="gray", linewidth=0.8)
    ax.set_xticks(x) 
    ax.set_xticklabels([f"{d}s*" if d in (1870, 2020) else f"{d}s" for d in summary.index])
    fig.text(0.01, 0.01, "* partial decade (1871-79, 2020-Jun 2026). Nominal, log returns summed.", fontsize=8)
    ax.set_ylabel("Cumulative log return")
    ax.set_title("S&P 500 by decade: earnings growth vs P/E multiple change")
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=150)

def plot_cumulative(df: pd.DataFrame, path: str) -> None:
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df["Date"], np.log(df["P"] / df["P"].iloc[0]), color="black", label="Price")
    ax.plot(df["Date"], np.log(df["E"] / df["E"].iloc[0]), color="#2a6f97", label="Earnings")
    ax.plot(df["Date"], np.log(df["PE"] / df["PE"].iloc[0]), color="#e07a5f", label="P/E multiple")
    ax.axhline(0, color="gray", linewidth=0.8)
    ax.set_ylabel("Cumulative log change since Jan 1871")
    ax.set_title("S&P 500 since 1871: price = earnings + multiple")
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=150)

def plot_pe_vs_cape(df: pd.DataFrame, path: str) -> None:
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df["Date"], df["PE"], color="#e07a5f", label="Trailing P/E (1-year earnings)")
    ax.plot(df["Date"], df["CAPE"], color="#2a6f97", label="CAPE (10-year real earnings)")
    ax.set_ylabel("Valuation multiple")
    ax.set_title("Trailing P/E vs CAPE: smoothing earnings removes the 2009 distortion")
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=150)

def plot_rolling_regime(df: pd.DataFrame, path: str) -> None:
    d = df.dropna(subset=["regime"])
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(d["Date"], d["ret_E_roll"], color="#2a6f97", label="Earnings (trailing 10y)")
    ax.plot(d["Date"], d["ret_PE_roll"], color="#e07a5f", label="P/E multiple (trailing 10y)")
    lo, hi = ax.get_ylim()
    ax.fill_between(d["Date"], lo, hi, where=(d["regime"] == "multiple-driven").values,
                    color="#e07a5f", alpha=0.12, label="Multiple-driven window")
    ax.set_ylim(lo, hi)
    ax.axhline(0, color="gray", linewidth=0.8)
    ax.set_ylabel("Trailing 10-year cumulative log change")
    ax.set_title("What drove the S&P 500 over each trailing 10 years")
    ax.legend(loc="upper left")
    fig.tight_layout()
    fig.savefig(path, dpi=150)