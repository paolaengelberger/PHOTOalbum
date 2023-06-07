import streamlit as st
import pandas as pd


st.title("Welcome to my first app")

st.markdown(":violet[This app will generate graphs from frequency tables ;)]")
df = pd.DataFrame(columns=["Dato", "Frecuencia"])

custom_num_rows = int(input("Enter the number of rows: "))

for _ in range(custom_num_rows):
    dato = st.text_input("Enter Dato")
    frecuencia = st.number_input("Enter Frecuencia", min_value=0, value=0, step=1)
    row = {"Dato": dato, "Frecuencia": frecuencia}
    df = df.append(row, ignore_index=True)

st.table(df)

favorite_command = df.loc[df["Frecuencia"].idxmax(), "Dato"]
