import pandas as pd
import plotly.express as px
import streamlit as st

DATA_PATH = "data/vehicles.csv"

st.header("Cuadro de mando: anuncios de venta de coches")

# Leer datos
car_data = pd.read_csv(DATA_PATH)

st.write("Dataset cargado. Filas y columnas:", car_data.shape)

# Botón 1: histograma
hist_button = st.button("Construir histograma (odometer)")

if hist_button:
    st.write("Creación de un histograma para la columna odometer")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón 2: dispersión
scatter_button = st.button("Construir gráfico de dispersión (odometer vs price)")

if scatter_button:
    st.write("Creación de un gráfico de dispersión: odometer vs price")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
