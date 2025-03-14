import streamlit as st
import os


def show():
    st.title("🐍 Welcome to PyMasters")
    st.write("The ultimate Python knowledge-sharing hub with futuristic UX!")

    logo_path = os.path.join(os.getcwd(), "assets/pymasters_logo.png")

    # Show logo in the sidebar
    with st.sidebar:
        if os.path.exists(logo_path):
            st.image(logo_path, width=200)
        else:
            st.warning("⚠️ Logo not found! Please check the assets folder.")
