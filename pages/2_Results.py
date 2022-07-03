import streamlit as st
import pandas as pd
from PIL import Image

st.markdown("# Second Step: Results")
st.sidebar.markdown("# Results")

def codigoSugerido():
    st.header('Analysis results')
    #st.text('10101501')  
    #st.text('90%') 
    st.subheader('10101501')
    st.subheader('90%')

    st.subheader('Classification')

    #st.table(columns= )

    df = pd.DataFrame(
    columns=('Percentage', 'Category', 'Detail')
    )

    row1 = ['70%', 'Segment', '10- Live Plant and Animal']
    row2 = ['90%', 'Family', '10- Live Animals']
    row3 = ['60%', 'Class', '15- Livestock']
    row4 = ['80%', 'Commodity', '01- Cats']

    df = df.append(pd.Series(row1, index=df.columns[:len(row1)]), ignore_index=True)
    df = df.append(pd.Series(row2, index=df.columns[:len(row2)]), ignore_index=True)
    df = df.append(pd.Series(row3, index=df.columns[:len(row3)]), ignore_index=True)
    df = df.append(pd.Series(row4, index=df.columns[:len(row4)]), ignore_index=True)

    st.table(df)




codigoSugerido()

