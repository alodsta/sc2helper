import asyncio
import streamlit as st
import numba


with st.sidebar:
    '**Some sidebar**'


with st.container():
    tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])


def action():
    st.session_state['clicker'] += 1


if 'clicker' not in st.session_state:
    st.session_state['clicker'] = 0

if 'name' in st.session_state and bool(st.session_state.name):
    st.write(f'hi, {st.session_state.name}')

st.session_state['name'] = st.text_input('What is ur name?')

st.button('reload', on_click=action)
f'cliker: {st.session_state.clicker}'
