import asyncio
import streamlit as st
import numba


if 'info' not in st.session_state:
    st.session_state['info'] = {
        'Zerg': {},
        'Terr': {},
        'Toss': {}
    }
else:
    st.session_state['info'] = st.session_state.info

st.write('Hello')
