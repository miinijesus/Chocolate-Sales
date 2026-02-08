import streamlit as st


from dataset import df
from chart import (
    chart_sales_by_year,
    chart_box_shipped_by_year,
    chart_sales_by_seller,
    chart_sales_by_product
)
from utils import format_number

st.set_page_config(
    page_title="Chocolate Sales Dashboard", layout="wide", page_icon="🍫"
)
st.title("Chocolate Sales Dashboard")

tab1, tab2, tab3, tab4 = st.tabs(
    ["Overview", "Total Sales", "Sales by Country", "Sales by Product"]
)

with tab1:
    st.header("Overview")
    st.write(
        "This dashboard provides insights into chocolate sales data. Use the tabs to explore sales by country and product."
    )
    st.dataframe(df)
with tab2:
    years = sorted(df["Year"].unique().tolist())
    years.insert(0, "All")

    year_selected = st.selectbox("Select Year", years)

    if year_selected == "All":
        df_filtered = df
    else:
        df_filtered = df[df["Year"] == year_selected]

    col1, col2, col3 = st.columns([25, 25, 50])
    with col1:
        st.metric("Total Sales", format_number(df_filtered["Amount"].sum(), prefix="$"))
        st.plotly_chart(
            chart_sales_by_year(df, year_selected), use_container_width=True
        )
    with col2:
        st.metric(
            "Total Box Shipped", format_number(df_filtered["Boxes Shipped"].sum())
        )
        st.plotly_chart(
            chart_box_shipped_by_year(df, year_selected), use_container_width=True
        )

    with col3:
        st.plotly_chart(chart_sales_by_seller(df_filtered, year_selected), use_container_width=True)

    st.plotly_chart(chart_sales_by_product(df_filtered), use_container_width=True)


with tab3:
    from tabs.Countries import render_countries_tab

    render_countries_tab()