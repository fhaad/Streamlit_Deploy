import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pylab as plt
import plotly.express as px
import datetime
from PIL import Image

image = Image.open('D:\Streamlit_Deploy\src\Olist1.png')
st.image(image, caption='', width=100)
st.title("Proyecto Final - Olist") 
st.text('Sitio web para explorar la visualizacion de Dashboard')

st.markdown('***')
st.header('Consultoría')
st.markdown('Análisis y aplicación de estrategias de Data Science a un conjunto de datasets para conocer el comportamiento general de ventas, compras, mercadeo y demás datos de interés de la plataforma')
st.markdown('***')
st.header('Objetivo General')
st.markdown('Realizar un proceso de Extracción, Transformación y Carga (ETL) de la información relativa a la actividad de la plataforma OLIST para la elaboración y análisis de KPIs y métricas que proporcionen información relevante para la toma de decisiones basada en inteligencia de negocios')
st.markdown('***')
#--------------------------------------------------------------------------------------#
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
#--------------------------------------------------------------------------------------#
# NAVEGADOR DE OPCIONES CON LA CARGA DE DATASET
st.sidebar.title('Navegador de Opciones')
uploaded_file = st.sidebar.file_uploader('Cargue su DATASET aqui')

options = st.sidebar.radio('Paginas', options=['Home','Ventas', 'Productos', 'Vendedores', 'Clientes', 'Marketing', 
                                                'Metodos de pago', 'Reviews', 'Delivery', 'App', 'Uber', 'Histograma'
                            
])

#---------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------#
# CARGA DE DATASET A DATAFRAME

if uploaded_file:
    dataset = pd.read_csv(uploaded_file)
#--------------------------------------------------------------------------------------#

st.header('Visualizacion de Dashboard')
dataset = pd.read_csv(r'D:\Streamlit_Deploy\Datasets\wine_reviews_clean.csv', sep = ',', encoding = 'utf_8')
filter1 = dataset['variety']
filter2 = dataset['points']
#---------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------#
# FUNCIONES PRINCIPALES
@st.cache
def Ventas(dataset):
    st.header('Dataset')
    st.dataframe(dataset)
#-------------------------------------------------------------------------------#
@st.cache
def stats(dataset):
    st.header('Data Statistics')
    st.write(dataset.describe())
#-------------------------------------------------------------------------------#
@st.cache
def data_header(dataset):
    st.header('Data Header')
    st.write(dataset.head(10))
#-------------------------------------------------------------------------------#
@st.cache
def plot(dataset):
    fig, ax=plt.subplot(1,1)
    ax.scatter(x=dataset['country'], y=dataset['points'])
    ax.set_xlabel('pais')
    ax.set_ylabel('puntos')
    st.pyplot(fig)
#-------------------------------------------------------------------------------#
@st.cache
def lines():
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
    st.line_chart(chart_data)
#-------------------------------------------------------------------------------#
@st.cache
def interactive_plot(dataset):
    x_axis_val = st.selectbox('Seleccione X-Eje Value', options=dataset.columns)
    y_axis_val = st.selectbox('Seleccione Y-Eje Value', options=dataset.columns)
    col = st.color_picker('Seleccione color de la grafica')
    plot = px.scatter(dataset, x=x_axis_val, y=y_axis_val)
    plot.update_traces(marker=dict(color=col))
    st.plotly_chart(plot)
#-------------------------------------------------------------------------------#
def histograma(dataset):
    st.subheader('Number of pickups by hour')
    hist_values = np.histogram(dataset[filter1], bins=24, range=(0,100))[4]
    st.bar_chart(hist_values)


#-------------------------------------------------------------------------------#
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)


#--------------------------------------------------------------------------------------#
# AREA DE OPCIONES PARA EJECUTAR LAS FUNCIONALIDADES y DE NAVEGACION
if options == 'Ventas':
    st.text('Podemos Observar el Dataset')
    Ventas(dataset)
elif options == 'Data Statistics':
    st.text('Despliegue de la estadistica general del Dataset')
    stats(dataset)
elif options == 'Data Header':
    st.text('Despliegue de los primeros 10 registros')
    data_header(dataset)
elif options == 'plot':
    st.text('Grafico de puntos')
    plot(dataset)
elif options == 'lineas':
    st.text('Grafico de lineas')
    lines()
elif options == 'Grafica Interactiva':
    st.text('Grafico Interactivo')
    interactive_plot(dataset)
elif options == 'Uber':
    st.text('Uber Interactivo')
    load_data(nrows)
elif options == 'Histograma':
    st.text('Grafico de Histograma')
    histograma(dataset)
#--------------------------------------------------------------------------------------#
