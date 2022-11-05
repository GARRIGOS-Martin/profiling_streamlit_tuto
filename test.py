import pandas as pd
import pandas_profiling as pp
import streamlit as st
from st_on_hover_tabs import on_hover_tabs
import os
from streamlit_pandas_profiling import st_profile_report



with st.sidebar: 
    st.image("./iiidata.png")
    st.title("AutoNickML")
    if st.button("Charger") : 
        file = st.file_uploader("Chargez vos données")
        if file: 
            df = pd.read_csv(file, index_col=None)
            df.to_csv('dataset.csv', index=None)
            st.dataframe(df)

    st.button("Analyser")
    st.button("Exporter")
   
    st.info("This project application helps you build and explore your data.")


