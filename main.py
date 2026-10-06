from src.data_loader import load_shiller_data
from src.decomposition import add_decomposition, add_cape, add_rolling_regime, decade_summary
from src.viz import plot_decade_decomposition, plot_cumulative, plot_pe_vs_cape, plot_rolling_regime

df = add_rolling_regime(add_cape(add_decomposition(load_shiller_data("data/raw/ie_data.xls"))))

plot_decade_decomposition(decade_summary(df), "outputs/decade_decomposition.png")
plot_cumulative(df, "outputs/cumulative.png")
plot_pe_vs_cape(df, "outputs/pe_vs_cape.png")
plot_rolling_regime(df, "outputs/rolling_regime.png")
print("Done: charts saved to outputs/")