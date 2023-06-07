import streamlit as st
import pandas as pd


st.title("Welcome to my first app")

st.markdown(":violet[This app will generate graphs from frequency tables ;)]")

df = pd.DataFrame(
    [
        {"Dato": None, "Frecuencia": None},
        {"Dato": None, "Frecuencia": None},
        {"Dato": None, "Frecuencia": None},
    ]
)

custom_num_rows = st.number_input("Enter the number of rows", min_value=1, value=0, type=int)
edited_df = pd.DataFrame(columns=["Dato", "Frecuencia"])

for _ in range(custom_num_rows):
    dato = st.text_input("Enter Dato")
    frecuencia = st.number_input("Enter Frecuencia", min_value=0, value=0, step=1)
    row = {"Dato": dato, "Frecuencia": frecuencia}
    edited_df = edited_df.append(row, ignore_index=True)

st.table(edited_df)

favorite_command = edited_df.loc[edited_df["Frecuencia"].idxmax(), "Dato"]