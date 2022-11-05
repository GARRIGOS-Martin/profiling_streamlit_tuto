import pandas as pd
import pandas_profiling as pp
import streamlit as st
from st_on_hover_tabs import on_hover_tabs
import os
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(layout="wide")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)
st.header("Overview d'un dataset en 2 clicks")

if os.path.exists('./dataset.csv'): 
    df = pd.read_csv('dataset.csv', index_col=None)

with st.sidebar:
    
    tabs = on_hover_tabs(tabName=['Charger les données', 'Analyser', 'Exporter'], 
                         iconName=['upload file', 'analytics', 'download'], default_choice=0)
    st.image("./iiidata.png")

if tabs == 'Charger les données':
    file = st.file_uploader("Chargez vos données")
    if file: 
        df = pd.read_csv(file, index_col=None)
        df.to_csv('dataset.csv', index=None)
        st.dataframe(df)

elif tabs == 'Analyser':
    st.title("Exploratory Data Analysis")
    profile_df = df.profile_report()
    st_profile_report(profile_df)
    profile_df.to_file("output.html")
    

elif tabs == 'Exporter':
    with open("output.html", 'rb') as f: 
        st.download_button("Download Model", f, "rapport_analyse_data.html")
    



