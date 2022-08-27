import asyncio
import streamlit as st
import numba


with st.sidebar:
    '**Some sidebar**'


with st.container():
    tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])


def action():
    pass


st.session_state.name = st.text_input()
st.session_state.cliker = 0

f'hi, {st.session_state.name}'
st.button('reload', on_click=lambda: (st.session_state.cliker := st.session_state.cliker + 1))
f'cliker: {st.session_state.cliker}'