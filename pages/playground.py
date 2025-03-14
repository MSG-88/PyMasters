import streamlit as st


def show():
    st.title("⚡ Python Playground")
    st.write("Run Python code in an embedded Jupyter Notebook!")

    jupyter_url = "https://jupyter.org/try-jupyter/lab/"

    st.markdown(f"""
        <iframe src="{jupyter_url}" width="100%" height="600px"></iframe>
    """, unsafe_allow_html=True)