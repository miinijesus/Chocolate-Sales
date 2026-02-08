import plotly.express as px
import plotly.graph_objects as go


def chart_sales_by_year(df, selected_year):
    df_year = (
        df.groupby('Year')['Amount']
        .sum()  
        .reset_index()
        .sort_values('Year')
    )
    colors = []

    for year in df_year['Year']:
        if selected_year == "All" or year == selected_year:
            colors.append('rgba(30,64,175,1)')
        else:
            colors.append('rgba(30,64,175,0.3)')

        fig = go.Figure(
            go.Bar(
                x=df_year['Year'],
                y=df_year['Amount'],
                marker_color=colors,
                width=0.5
            )
        )
        fig.update_layout(
        yaxis_title='Total Sales ($)',
        )
        fig.update_xaxes(type='category')
    return fig


def chart_box_shipped_by_year(df, selected_year):
    df_year = (
        df
        .groupby('Year')['Boxes Shipped']
        .sum()
        .reset_index()
        .sort_values('Year')
    )
    color = []
    for year in df_year["Year"]:
        if selected_year == "All" or year == selected_year:
            color.append('rgba(30,64,175,1)')
        else:
            color.append('rgba(190,90,275,0.3)')
        
    fig = go.Figure(
        go.Bar(
            x=df_year['Boxes Shipped'],
            y=df_year['Year'],
                marker_color=color,
                width=0.5,
                orientation='h'
            )
        )
    
    fig.update_yaxes(type='category')
    return fig  


def chart_sales_by_seller(df_filtered, selected_year):
    if selected_year != "All":
        df_filtered = df_filtered[df_filtered["Year"] == selected_year]
        
    df_seller = (
        df_filtered
        .groupby("Sales Person")["Amount"]
        .sum()
        .reset_index()
        .head(10)
        .sort_values("Amount", ascending=False)
    )

    fig = px.bar(
        df_seller,
        x="Sales Person",
        y="Amount",
        title="Sales by Seller",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
   
    return fig

def chart__sales_by_seller_country(df, selected_year):
    if selected_year != "All":
        df = df[df["Year"] == selected_year]
        
    df_seller_country = (
        df
        .groupby(["Country", "Sales Person"])["Amount"]
        .sum()
        .reset_index()
        .sort_values("Amount", ascending=False) 
    )
    
    fig = px.bar(
        df_seller_country,
        x="Sales Person",
        y="Amount", 
        color="Country",
        title="Sales by Seller and Country",
        color_discrete_sequence = px.colors.qualitative.Pastel2
    )
    fig.update_xaxes(type='category')
    return fig


def chart_sales_by_product(df_filtered):
    df_product = (
        df_filtered
        .groupby("Product")["Amount"]
        .sum()
        .reset_index()
        .head(10)
        .sort_values("Amount", ascending=False)
    )

    fig = px.bar(
        df_product,
        x="Product",
        y="Amount",
        title="Sales by Product",
        color="Product",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    return fig