from msilib.schema import Icon
import pandas as pd
import pandas_profiling
import streamlit as st
from st_on_hover_tabs import on_hover_tabs
import os
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(layout="wide", page_title="IIIDATA TUTO")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)
# git, linkedin = st.columns(2)
# git.markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/GARRIGOS-Martin/profiling_streamlit_tuto)")
# git.info("Récupérez l'intégralité du code ici")
# linkedin.markdown("[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/company/iiidata/?viewAsMember=true)")
# linkedin.info("N'hésitez pas à nous suivre sur Linkedin ")

st.header("  Faites une première analyse automatisée de vos données ")


if os.path.exists('./dataset.csv'): 
    df = pd.read_csv('dataset.csv', index_col=None)

with st.sidebar:
    
    tabs = on_hover_tabs(tabName=['Charger les données', 'Analyser', 'Exporter'], 
                         iconName=['upload file', 'analytics', 'download'], default_choice=0)
    st.image("./iiidata.png")

if tabs == 'Charger les données':
    file = st.file_uploader("Chargez vos données")
    separator = st.radio("Si votre dataset ne s'affiche pas correctement, sélectionner le bon séparateur", [",", ";"])
    if file: 
        df = pd.read_csv(file, index_col=None, sep = separator)
        df.to_csv('dataset.csv', index=None)
        if len(df.columns) >= 2 : 
            st.success("Données chargées correctement, vous pouvez passer à l'analyse")
        else : 
            st.error('Il semblerait que vous avez sélectionné le mauvais séparateur')
        st.dataframe(df)
    st.image("./background.png")
        
        

elif tabs == 'Analyser':
    st.title("Exploratory Data Analysis")
    profile_df = df.profile_report()
    st_profile_report(profile_df)
    profile_df.to_file("output.html")
    

elif tabs == 'Exporter':
    with open("output.html", 'rb') as f: 
        dw = st.download_button("Télécharger le rapport ", f, "rapport_analyse_data.html")
        if dw : 
            st.balloons()
    
    st.image("./background.png")
    



