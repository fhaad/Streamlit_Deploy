import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pylab as plt

st.title('Introducción a Streamlit')
st.text('Sitio web para explorar la visualizacion de graficos')
st.markdown('***')

# aqui vamos a cargar un DataFrame y mostrarlo en streamlit localmente

# ruta de los datasets
dataset = pd.read_csv(r'D:\Streamlit_Deploy\Datasets\wine_reviews.csv', sep = ',', encoding = 'utf_8')
#st.dataframe(dataset) # Con esta instruccion se muestra el DataFrame

def data(dataset):
    st.header('Dataset')
    st.dataframe(dataset)

def stats(dataset):
    st.header('Data Statistics')
    st.write(dataset.describe())

def data_header(dataset):
    st.header('Data Header')
    st.write(dataset.head(10))

def plot(dataset):
    fig, ax=plt.subplot(1,1)
    ax.scatter(x=dataset['country'], y=dataset['points'])
    ax.set_xlabel('pais')
    ax.set_ylabel('puntos')
    st.pyplot(fig)

def lines():
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

    st.line_chart(chart_data)



st.sidebar.title('Navegador')
uploaded_file = st.sidebar.file_uploader('Cargue su archivo aqui')

options = st.sidebar.radio('Paginas', options=['Home', 'Dataset', 'Data Statistics', 'Data Header', 'plot', 'lineas'])

if uploaded_file:
    dataset = pd.read_csv(uploaded_file)


if options == 'Dataset':
    st.text('Podemos Observar el Dataset')
    data(dataset)
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





st.sidebar.markdown('Introducción sobre los usos y ventajas de Streamlit')

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )








