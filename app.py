import streamlit as st 
import pandas as pd

st.title("Welcome to my first app")

st.markdown(" :violet[This app will generate graphs from frecuency tables ;)]")  


df = pd.DataFrame(
    [
        {"Dato": "Dato 1", "Frecuencia": 0, },
        {"Dato": "Dato 2", "Frecuencia": 0, },
        {"Dato": "Dato 2", "Frecuencia": 0, },
    ]
) 

custom_num_rows = st.number_input("Enter the number of rows", min_value=1, value=len(df))
edited_df= st.data_editor(df, num_rows="dynamic") 
favorite_command = edited_df.loc[edited_df["Frecuencia"].idxmax()]["Dato"]


