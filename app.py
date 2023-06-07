import streamlit as st
import pandas as pd
import numpy as np

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
edited_df = df.head(custom_num_rows)
st.table(edited_df)
