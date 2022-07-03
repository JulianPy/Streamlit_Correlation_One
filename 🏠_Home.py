import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide",
)


st.sidebar.markdown("# Home")

header = st.container()
dataset = st.container()
features = st.container()
modelTraining = st.container()


def imagen():
    image = Image.open('home.png')
    st.image(image, caption='')
    image2 = Image.open('home2.png')
    st.image(image2, caption='')


imagen()