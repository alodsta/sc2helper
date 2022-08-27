import streamlit as st

from models import SCObject


obj = SCObject(_id='qwerty')
st.write(obj.json())
