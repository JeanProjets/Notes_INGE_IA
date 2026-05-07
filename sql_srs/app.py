import streamlit as st
import pandas as pd

tab1, tab2, tab3 = st.tabs(["cat", "dog", "owl"])

df = pd.DataFrame({"a" : [1, 2, 3], "b" : [4, 5, 6]})
with tab1:
    input_text = st.text_area('Write something')
    st.write('You wrote:', input_text)
    st.dataframe(df)

with tab2:
    st.header('A dog')
    st.image('https://static.streamlit.io/examples/dog.jpg', width=200)

with tab3:
    st.header('An owl')
    st.image('https://static.streamlit.io/examples/owl.jpg', width=200)
