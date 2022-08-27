import streamlit as st

from models import SCObject


obj = SCObject(some_id=123)
st.write(obj.json())
