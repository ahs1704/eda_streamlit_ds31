import streamlit as st
import plotly.express as px
import pandas as pd
import warnings
import os
warnings.filterwarnings("ignore")

st.set_page_config(page_title="Superstore Dashboard", layout="wide", page_icon="📊")
st.title("📊 Superstore EDA Dashboard")
st.markdown('<style>div.block-container{padding-top: 1rem;}</style>', unsafe_allow_html=True)

fl = st.file_uploader(":file_folder: Upload a file", type=["csv", "xlsx", "json"], label_visibility="collapsed")
if fl is not None:
    df = pd.read_csv(fl)
else:
    if not os.path.exists("Sample - Superstore.csv"):
        st.warning("File 'Sample - Superstore.csv' tidak ditemukan. Silakan download dari [Kaggle](https://www.kaggle.com/datasets/jessemostipak/superstore-dataset) dan letakkan di folder ini.")
        st.stop()
    df = pd.read_csv("Sample - Superstore.csv", encoding="ISO-8859-1")

col1, col2 = st.columns(2)
df["Order Date"] = pd.to_datetime(df["Order Date"])
startDate = pd.to_datetime(df["Order Date"].min())
endDate = pd.to_datetime(df["Order Date"].max())

with col1:
    date1 = pd.to_datetime(st.date_input("Start Date", startDate))
with col2:
    date2 = pd.to_datetime(st.date_input("End Date", endDate))

df = df[(df["Order Date"] >= date1) & (df["Order Date"] <= date2)].copy()

region = st.sidebar.multiselect("Pick your Region", df["Region"].unique())
if not region:
    df2 = df.copy()
else:
    df2 = df[df["Region"].isin(region)].copy()

state = st.sidebar.multiselect("Pick your State", df2["State"].unique())
if not state:
    df3 = df2.copy()
else:
    df3 = df2[df2["State"].isin(state)].copy()

city = st.sidebar.multiselect("Pick your City", df3["City"].unique())
if not city:
    filtered_df = df3.copy()
else:
    filtered_df = df3[df3["City"].isin(city)].copy()

category_df = filtered_df.groupby(by=["Category"], as_index=False)["Sales"].sum()

with col1:
    st.subheader("Category Sales")
    fig = px.bar(category_df, x="Category", y="Sales", color="Category",
                 text=category_df["Sales"].apply(lambda x: f"${x:,.2f}"),
                 title="Total Sales by Category", template="seaborn")
    st.plotly_chart(fig, use_container_width=True)
with col2:
    st.subheader("Sales by Region")
    fig = px.pie(filtered_df, values="Sales", names="Region", hole=0.5)
    fig.update_traces(text=filtered_df["Region"], textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

filtered_df["month_year"] = filtered_df["Order Date"].dt.to_period("M")
st.subheader('Time Series Analysis')

linechart = pd.DataFrame(filtered_df.groupby(filtered_df["month_year"].dt.strftime("%Y : %b"))["Sales"].sum()).reset_index()
fig2 = px.line(linechart, x = "month_year", y = "Sales", labels = {"Sales": "Amount"}
               , height=500, width=1000, template="gridon")
st.plotly_chart(fig2, use_container_width=True)

with st.expander("View Data of Tiem Series Analysis"):
    st.write(linechart.T.style.background_gradient(cmap='Blues'))
    csv = linechart.to_csv(index=False).encode("utf-8")
    st.download_button('Download Data', data = csv, file_name = "TimeSeries.csv", mime = "text/csv")

#create a tree map based on region , category and sub-category
st.subheader("Tree Map of Sales by Region, Category and Sub-Category")
fig3 = px.treemap(filtered_df, path=["Region", "Category", "Sub-Category"], values="Sales",
                  color="Sub-Category", hover_data=["Sales"],
                  color_continuous_scale=px.colors.sequential.RdBu)
fig3.update_layout(width = 800, height = 650)
st.plotly_chart(fig3, use_container_width=True)

chart1, chart2 = st.columns(2)
with chart1:
    st.subheader("Segment wise Sales")
    fig = px.pie(filtered_df, values = "Sales", names = "Segment", template = "gridon")
    fig.update_traces(text = filtered_df["Segment"], textposition = "inside")
    st.plotly_chart(fig, use_container_width=True)
with chart2:
    st.subheader("Category wise Sales")
    fig = px.pie(filtered_df, values = "Sales", names = "Category", template = "plotly_dark")
    fig.update_traces(text = filtered_df["Category"], textposition = "inside")
    st.plotly_chart(fig, use_container_width=True)

import plotly.figure_factory as ff
st.subheader(":point_right: Month wise Sub-Category Sales Summary")
with st.expander("Summary_Table"):
    df_sample = df[0:5][["Region", "State", "City", "Category", "Sub-Category", "Sales", "Profit","Quantity"]]
    fig = ff.create_table(df_sample, colorscale = "Cividis", height_constant = 20)
    st.plotly_chart(fig, use_container_width=True)



st.write("Data Source: [Kaggle - Superstore Dataset](https://www.kaggle.com/datasets/jessemostipak/superstore-dataset)")