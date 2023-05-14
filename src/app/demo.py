import streamlit as st
from src.ner import build_entity

st.image("https://www.rosette.com/wp-content/uploads/2022/03/header-img-event-extraction@2x.png")
st.header('Find Named Entitiy')

text = st.text_input('Enter Your Text')

gen_button = st.button('Generate')
if gen_button ==True:
    st.dataframe(build_entity(text))
    

