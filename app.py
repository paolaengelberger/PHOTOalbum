import streamlit as st
import pandas as pd

st.title("Welcome to my first app")
st.markdown(":violet[This app will generate graphs from frequency tables ;)]")

df = pd.DataFrame(columns=["Dato", "Frecuencia"])

custom_num_rows = st.number_input("Enter the number of rows", min_value=1, value=1, step=1, key="num_rows")

min_value = st.number_input("Enter the minimum value", value=0, key="min_value")
max_value = st.number_input("Enter the maximum value", value=1, key="max_value")

if min_value >= max_value:
    st.error("Minimum value should be less than the maximum value.")

for _ in range(custom_num_rows):
    row = {"Dato": None, "Frecuencia": None}
    df = df.append(row, ignore_index=True)

editable_df = st.dataframe(df, editable=True)

favorite_command = editable_df.loc[editable_df["Frecuencia"].idxmax(), "Dato"]

