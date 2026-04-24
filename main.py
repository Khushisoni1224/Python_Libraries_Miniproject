import streamlit as st
from python_pages.python_ui import show_python
from numpy_page import show_numpy
from matplotlib_page import show_matplotlib
from pandas_page import show_pandas

st.title("Interactive Python Learning Tool")

tab1, tab2, tab3, tab4= st.tabs(["🐍 Python", "🔢 NumPy", "📊 Matplotlib", "🐼Pandas"])

with tab1:
    show_python()

with tab2:
    show_numpy()
with tab3:
    show_matplotlib()
with tab4:
    show_pandas()

#python -m streamlit run main.py