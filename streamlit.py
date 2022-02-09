import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from config import *

# Basic Configuration
st.set_page_config(
    page_title="Investment Tracker",
    page_icon="💸",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Query de Database and turn it into a Pandas DataFrame
url = "postgresql://{}:{}@{}:{}/{}".format(
    PG_user, PG_password, PG_host, PG_port, PG_dbname
)
engine = create_engine(url)
df = pd.read_sql_query("Select * from investments", engine)
df = df.sort_values(by=["Date"], ascending=False).reset_index(drop=True)


# App title
st.title("Investments App")

# Balance
col1, col2, col3 = st.columns(3)
col1.metric("Total", str(df.Total[0]) + "€", str(df.Total[0] - df.Total[6]) + "€")
col2.metric(
    "Coinbase", str(df.Coinbase[0]) + "€", str(df.Coinbase[0] - df.Coinbase[6]) + "€"
)
col3.metric("Indexa", str(df.Indexa[0]) + "€", str(df.Indexa[0] - df.Indexa[6]) + "€")

# Chart
st.area_chart(df[["Coinbase", "Indexa", "Date"]].set_index("Date"))

# Last 5 days
st.header("Last 5 days dropdown")
st.table(df.head())
