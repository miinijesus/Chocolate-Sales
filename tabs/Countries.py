import streamlit as st
from dataset import df
from chart import (
    chart_sales_by_year,
    chart_box_shipped_by_year,
    chart_sales_by_product,
    chart__sales_by_seller_country
)
from utils import format_number


def render_countries_tab():

    if "year" not in st.session_state:
        st.session_state["year"] = "All"



    col1, col2 = st.columns([50, 50])
    with col1:
        years = sorted(df["Year"].unique().tolist())
        years.insert(0, "All")
        
        year = st.selectbox("Select Year", years, key="years")
    

    with col2:
        countries = sorted(df["Country"].unique().tolist())
        country_selected = st.selectbox("Select Country", countries, key="countries")
   
    df_country_all_years = df[df["Country"] == country_selected]
    
    if year == "All":
        df_country_year = df_country_all_years
    else:
        df_country_year = df_country_all_years[
            df_country_all_years["Year"] == year
        ]
        
    st.caption(f"Sales data for {country_selected} in {year}")
    
    col3, col4 = st.columns([50, 50])
    with col3:
        st.metric(
            "Total Sales",
            format_number(df_country_year["Amount"].sum(), prefix="$"),
        )
    with col4:
        st.metric("Total Box Shipped", format_number(df_country_year["Boxes Shipped"].sum()))

    st.divider()
    col5, col6, col7 = st.columns([25, 25, 50])
    with col5:
        st.plotly_chart(chart_sales_by_year(df_country_all_years, year), use_container_width=True)
    with col6:
        st.plotly_chart(
            chart_box_shipped_by_year(df_country_all_years, year), use_container_width=True
        )
    with col7:
        st.plotly_chart(
            chart_sales_by_product(df_country_all_years), use_container_width=True
        )
    st.plotly_chart(
        chart__sales_by_seller_country(df_country_all_years, year), use_container_width=True
    )