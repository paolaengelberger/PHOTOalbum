import streamlit as st
import pandas as pd

st.title("Welcome to my first app")
st.markdown(":violet[This app will generate graphs from frequency tables ;)]")

df = pd.DataFrame(columns=["Dato", "Frecuencia"])

custom_num_rows = int(input("Enter the number of rows: "))

user_input = st.text_area("Enter Dato and Frecuencia (separated by a comma)", height=custom_num_rows)

rows = user_input.split("\n")

for row in rows:
    values = row.split(",")
    if len(values) == 2:
        dato = values[0].strip()
        frecuencia = int(values[1].strip())
        df = df.append({"Dato": dato, "Frecuencia": frecuencia}, ignore_index=True)

st.table(df)

favorite_command = df.loc[df["Frecuencia"].idxmax(), "Dato"]