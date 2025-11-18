import streamlit as st
import pandas as pd
from sqlalchemy import text
from warehouse.postgres_client import engine

st.set_page_config(page_title="ETL Dashboard")
st.title("Sales Analytics Dashboard")

with engine.connect() as conn:
    df = pd.read_sql(
        text("SELECT *, quantity * unit_price AS revenue FROM sales ORDER BY order_date DESC"),
        conn
    )

if df.empty:
    st.info("No data found. Run ETL first.")
else:
    st.dataframe(df)
    st.line_chart(df.groupby("order_date")["revenue"].sum())
