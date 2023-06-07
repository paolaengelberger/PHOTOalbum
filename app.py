import streamlit as st
import pandas as pd

st.title("Welcome to my first app")
st.markdown(":violet[This app will generate graphs from frequency tables ;)]")

df = pd.DataFrame(columns=["Dato", "Frecuencia"])

custom_num_rows = st.number_input("Enter the number of rows", min_value=1, value=0, step=1, key="num_rows")

for _ in range(custom_num_rows):
    row = {"Dato": None, "Frecuencia": None}
    df = df.append(row, ignore_index=True)

editable_df = st.dataframe(df, editable=True)

favorite_command = editable_df.loc[editable_df["Frecuencia"].idxmax(), "Dato"]
