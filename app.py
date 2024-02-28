import streamlit as st
import pandas as pd
import plotly_express as px

st.header('Aplicación Web - Anuncios de Autos')
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Histograma Interactivo') # crear un botón
scatter_button = st.button('Gráfico Interactivo')

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Crea un histograma para el conjunto de datos de anuncios de venta de coches')

# crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatter_button: # Si se hace clic en el botón de gráfico de dispersión
    # Escribir un mensaje
    st.write('Crea un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión
    fig = px.scatter(car_data, x="model_year", y="price")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

