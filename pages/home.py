import streamlit as st
import pandas as pd
from PIL import Image
st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")

def cabecera():
    st.title("Colombia Compra Eficiente")

def botoncito():
    # Cargar el Archivo
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # Lectura del Archivo
        #st.write("filename:", uploaded_file.name)
        st.subheader('Validation Table')
        df1 = pd.read_excel(uploaded_file)
        st.dataframe(df1)
        st.markdown('A validation table is shown with the complete results of the classification.'
                    ' It gives you a suggestion to change your **UNSPC** code or a recommendation'
                    ' for your contract ')
        st.subheader('Words Count')
        # Grafica
        #g = df1['Sale Price']
        #st.line_chart(g)


            #bytes_data = uploaded_file.read()
            #st.write("filename:", uploaded_file.name)
            #st.write(bytes_data)
            #st.write('Buena may')
            #data = {'Contract number':[123456, 24561012, 369121518, 48121620, 510152025],
            #        'Contract Type': ['Food', 'Integral Services', 'Construction materials', 'Health', 'Others'],
            #        'Probability': [0.99, 0.97, 0.94, 0.90, 0.85]}
            #df = pd.DataFrame(data)
def codigoSugerido():
    st.header('Analysis results')

cabecera()
botoncito()
codigoSugerido()