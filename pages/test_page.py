import streamlit as st

if 'my_number' in st.session_state and st.session_state.my_number:
    st.write(f'Number is {st.session_state.my_number}')
else:
    st.write('Number does not set, yet')
