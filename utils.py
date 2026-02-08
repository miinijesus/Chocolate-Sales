import pandas as pd
import streamlit as st

from dataset import df

def format_number(value, prefix = ''):
    units = ['', 'K', 'M', 'B', 'T']
    for unit in units:
        if abs(value) < 1000:
            return f'{prefix}{value:.2f}{unit}'
        value /= 1000
    return f'{prefix}{value:.2f}'



# Total Revenue Tab

# Sales by Year
@st.cache_data
def sales_by_year(df):
    df_sales_year = (
        df.set_index('Date')
        .groupby(pd.Grouper(freq='Y'))['Amount']
        .sum()
        .reset_index()
    )
    
    return df_sales_year
