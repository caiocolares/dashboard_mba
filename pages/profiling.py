import streamlit as st
import pandas as pd
import plotly.express as px

import ydata_profiling
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report



def load_data(file_name):
    df = pd.read_csv(file_name)
    df['TEMPO'] = pd.to_datetime(df['TEMPO'])
    df['UF'] = df['LOCAL'].apply(lambda x: x.split('-')[-1] if len(x.split('-')[-1]) != 2 else 'ND' )


    pr = ProfileReport(df)
    st_profile_report(pr)




tab1, tab2, tab3 = st.tabs(["IByte","Nagem","Hapvida"])


with tab1:
    load_data('./dados/RECLAMEAQUI_IBYTE.csv')
with tab2:
    load_data('./dados/RECLAMEAQUI_NAGEM.csv')
with tab3:
    load_data('./dados/RECLAMEAQUI_HAPVIDA.csv')

