import streamlit as st
import pandas as pd
from PIL import Image

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

st.markdown("# Second Step: Results")
st.sidebar.markdown("# Results")

st.markdown('Here you will find the code that best suits your contract. The suggestion is given until class, to complete the last 2 digits of your code, we recommend you access the Colombia Compra Eficiente page where you can find the codes for products: [Classifier of goods and services](https://www.colombiacompra.gov.co/clasificador-de-bienes-y-Servicios) ')
col1f,col2f = st.columns(2)
col1f.subheader('Best code')
col2f.metric('98%', '101015')

col1,col2,col3 = st.columns(3)
col1.metric('Segment', '10', '70%')
col2.metric('Family', '10', '90%')
col3.metric('Class', '15', '60%')



