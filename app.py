import streamlit as st


with st.sidebar:
    '**Some sidebar**'

with st.container():
    tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
    st.button('Add new')

