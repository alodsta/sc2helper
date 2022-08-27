import asyncio
import streamlit as st
import numba


with st.sidebar:
    '**Some sidebar**'


with st.container():
    tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])


# def action():
#     st.session_state['clicker'] += 1


st.number_input('Choose number', key='my_number')
