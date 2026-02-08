import pandas as pd

df = pd.read_csv('data/ChocolateSales.csv')

df["Date"] = pd.to_datetime(df["Date"], format='%d/%m/%Y')

#creating year column
df["Year"] = df["Date"].dt.year

#creating month column
df["Month"] = df["Date"].dt.strftime('%b')
df["Month_num"] = df["Date"].dt.month

#cleaning money column
df["Amount"] = (
    df['Amount']
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(float)
)

