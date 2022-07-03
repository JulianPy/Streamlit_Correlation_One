import streamlit as st
import pandas as pd
from PIL import Image


st.markdown("# First Step: Upload your contract")
st.sidebar.markdown("# First Step: Upload your contract")

def parte1():
    st.title("Colombia Compra Eficiente")

    st.markdown("Welcome to this page. In it you will find a series of instructions that will allow you to know"
                " the United Nations code from the contract that is uploaded."
                " Before giving you the instructions for the use of this page, "
                " we must clarify that the file to be used must be in xlsx or csv format so that our"
                " algorithm can carry out the process of extracting, classifying and loading the result.")

    st.subheader('1.Select the file.')
    st.markdown("At this point you must upload the contract in the aforementioned formats"
                " in order to carry out the corresponding classification.")

    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        # Lectura del Archivo
        # st.write("filename:", uploaded_file.name)
        st.subheader('Validation Table')
        df1 = pd.read_excel(uploaded_file)
        st.dataframe(df1)
        st.markdown('A validation table is shown with the complete results of the classification.'
                    ' It gives you a suggestion to change your **UNSPC** code or a recommendation'
                    ' for your contract ')


parte1()
