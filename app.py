import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('notebooks/vehicles.csv')  # Lendo os dados

st.header('Análise de Dados de Veículos')  # Título do aplicativo

hist_button = st.button('Criar histograma')  # Criar um botão

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de Análise de Dados de Veículos')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
