import streamlit as st

import pandas as pd
import plotly.express as px

from streamlit_extras.app_logo import add_logo

st.set_page_config(layout="wide", menu_items={"About":"#Nothing realy good"})
st.title('Reclamações por período')


add_logo("https://upload.wikimedia.org/wikipedia/commons/e/e9/Logo_unifor_3.png", height=80)

st.sidebar.title("MBA Unifor")
st.sidebar.write("Trabalho da disciplina Dashboards em Python")
st.sidebar.divider()

st.sidebar.write("Desenvolvido por Caio Colares")
st.sidebar.write("colares.caio@gmail.com")

key = 0
def load_data(file_name):
    df = pd.read_csv(file_name)
    df['TEMPO'] = pd.to_datetime(df['TEMPO'])
    df['UF'] = df['LOCAL'].apply(lambda x: x.split('-')[-1] if len(x.split('-')[-1]) != 2 else 'ND' )

    col1, col2, col3 = st.columns(3)
    global key
    key += 1
    with col1:
        ano = st.selectbox('Ano', index=None, placeholder="Selecione um ano", options=df['ANO'].unique())
    with col2:
        estado  = st.selectbox('UF',index=None, placeholder="Selecione um estado", options=df['UF'].unique())
    with col3:
        chart_kind = st.selectbox("Tipo e Gráfico",  options=["Barra", "Linha"], key=key)

    df_filtered = df
    if ano:
        df_filtered = df_filtered[df_filtered['ANO'] == ano]
    if estado:
        df_filtered = df_filtered[(df_filtered['UF']== estado)]
    df_grouped = df_filtered.groupby(['ANO', 'MES'], as_index=False)['ID'].count()

    if chart_kind == 'Barra':
        fig = px.bar(df_grouped, x="MES", y="ID", color="ANO", 
                      title="Reclamações",
                      labels={
                            "ID": "Reclamações no período",
                            "ANO": "Ano",
                            "MES": "Mês"
                        })
    else:
        fig = px.line(df_grouped, x="MES", y="ID", color="ANO", 
                      markers=True, 
                      title="Reclamações",
                      labels={
                            "ID": "Reclamações no período",
                            "ANO": "Ano",
                            "MES": "Mês"
                        })
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df_filtered)




tab1, tab2, tab3 = st.tabs(["IByte","Nagem","Hapvida"])


with tab1:
    load_data('./dados/RECLAMEAQUI_IBYTE.csv')
with tab2:
    load_data('./dados/RECLAMEAQUI_NAGEM.csv')
with tab3:
    load_data('./dados/RECLAMEAQUI_HAPVIDA.csv')

