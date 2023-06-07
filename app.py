import streamlit as st 
import pandas as pd

st.title("Welcome to my first app")

st.markdown(" :violet[This app will generate graphs from frecuency tables ;)]")  


df = pd.DataFrame(
    [
        {"command": "Dato 1", "Frecuencia":0, },
        {"command": "Dato 2", "Frecuencia":0 , },
        {"command": "Dato 3", "Frecuencia":0, },
    ]
) edited_df = st.data_editor(df, num_rows="dynamic")


