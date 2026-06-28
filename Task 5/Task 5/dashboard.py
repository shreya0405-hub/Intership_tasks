import pandas as pd
import streamlit as st
import plotly.express as px

# Page Title
st.title("Interactive Business Dashboard")

# Load Dataset
df = pd.read_csv("data/sales_dashboard_data.csv")

# Sidebar Filter
st.sidebar.header("Filter Data")

region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + list(df["Region"].unique())
)

# Apply Filter
if region != "All":
    filtered_df = df[df["Region"] == region]
else:
    filtered_df = df

# KPI Metrics
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
average_sales = filtered_df["Sales"].mean()

# Display KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales}")
col2.metric("Total Profit", f"${total_profit}")
col3.metric("Average Sales", f"${average_sales:.2f}")

# Sales Trend Chart
st.subheader("Monthly Sales Trend")

sales_chart = px.line(
    filtered_df,
    x="Month",
    y="Sales",
    color="Category",
    markers=True,
    title="Sales Trend"
)

st.plotly_chart(sales_chart)

# Profit by Category
st.subheader("Profit by Category")

profit_chart = px.bar(
    filtered_df,
    x="Category",
    y="Profit",
    color="Category",
    title="Category Profit"
)

st.plotly_chart(profit_chart)

# Regional Sales Pie Chart
st.subheader("Sales Distribution")

pie_chart = px.pie(
    filtered_df,
    names="Category",
    values="Sales",
    title="Sales Share"
)

st.plotly_chart(pie_chart)

# Dataset Preview
st.subheader("Dataset Preview")
st.dataframe(filtered_df)