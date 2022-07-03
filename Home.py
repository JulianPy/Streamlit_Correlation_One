import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home",
    page_icon="chart_with_upwards_trend",
    layout="wide",
)



with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

st.sidebar.markdown("# Home")


header = st.container()
dataset = st.container()
features = st.container()
modelTraining = st.container()


def imagen():
    image = Image.open('home.png')
    st.image(image, caption='')
imagen()