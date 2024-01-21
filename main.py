import streamlit as st

import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", menu_items={"About":"#Nothing realy good"})

st.title('MBA Unifor - Dashboards Python')

df = pd.read_csv('./dados/RECLAMEAQUI_IBYTE.csv')
df['TEMPO'] = pd.to_datetime(df['TEMPO'])

ano = st.sidebar.selectbox('Ano', options=df['ANO'].unique())


df ['UF']= df['LOCAL'].apply(lambda x: x.split('-')[-1])
estado  = st.sidebar.selectbox('UF', options=df['UF'].unique())

df_filtered = df[(df['ANO'] == ano) & (df['UF']== estado)]

st.dataframe(df_filtered)

df_grouped = df.groupby(['ANO'], as_index=False)['ID'].count()
st.line_chart(df_grouped, x="ANO", y="ID")

st.snow()