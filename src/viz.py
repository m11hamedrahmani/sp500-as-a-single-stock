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