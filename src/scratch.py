# %%
import pandas as pd

df = pd.read_excel("/Users/mohamedrahmani/Desktop/portfolio/projets/sp500_PE/data/raw/ie_data.xls", sheet_name="Data", skiprows=7)
df.columns
# %%
df.head()
# %%
df.tail(10)

# %%
df.info()
# %%
df = df[['Date','P', 'D', 'E', 'CPI']]
df.columns
# %%
df.shape
# %%
## subset E
df.dropna(subset=["E"])
# %%
## subset E,D
df.dropna(subset=["E","D"])
# %%
df["Date"].head(12)
# %%
print(df["Date"].iloc[9])
# %%
formatted_date = f"{df["Date"].iloc[9]:.2f}"
month = formatted_date[5:7]
year = formatted_date[0:4]
print(f"{month},{year}")


# %%
df = df.dropna(subset=["E"])
date_str = df["Date"].map(lambda x: f"{x:.2f}")
df["Date"] = pd.to_datetime(date_str.str.slice(0, 4) + "-" + date_str.str.slice(5, 7) + "-01")
df = df.sort_values("Date").reset_index(drop=True)

print(df.shape)
print(df.head(12))
print(df.tail(3))
print(df.dtypes)
# %%
df[["P", "CPI"]] = df[["P", "CPI"]].astype(float)
print(df.dtypes)
print(df.isna().sum())
print(df.describe())
# %%