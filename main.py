import streamlit as st
from python_pages.python_ui import show_python
from numpy_page import show_numpy
from matplotlib_page import show_matplotlib

st.title("Interactive Python Learning Tool")

tab1, tab2, tab3 = st.tabs(["🐍 Python", "🔢 NumPy", "📊 Matplotlib"])

with tab1:
    show_python()

with tab2:
    show_numpy()

with tab3:
    show_matplotlib()