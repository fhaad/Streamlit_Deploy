import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pylab as plt

st.title('Introducción a Streamlit')
st.markdown('***')

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