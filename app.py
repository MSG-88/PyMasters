import streamlit as st
import os
from pages import home, knowledge_hub, chatbot, playground, leaderboard

# Set page config
st.set_page_config(page_title="PyMasters - Python Knowledge Hub", page_icon="🐍", layout="wide")

# Custom CSS for futuristic styling
st.markdown(
    """
    <style>
        body {background-color: #0f172a; color: white; font-family: 'Arial';}
        .stApp {background-color: #0f172a;}
        h1, h2, h3 {color: #38bdf8;}
        .sidebar .sidebar-content {background-color: #1e293b;}
    </style>
    """,
    unsafe_allow_html=True
)

# Tab-based navigation
tabs = st.tabs(["Home", "Knowledge Hub", "Chatbot", "Playground", "Leaderboard"])

st.markdown(
        """
        <style>
        div[role="tablist"] button {
            color: #38bdf8 !important; /* Futuristic Blue Font Color */
            font-weight: bold;
        }
        [data-testid="stSidebarNav"] {display: none;}
        </style>
        """,
        unsafe_allow_html=True
    )

with tabs[0]:
    home.show()

with tabs[1]:
    knowledge_hub.show()

with tabs[2]:
    chatbot.show()

with tabs[3]:
    playground.show()

with tabs[4]:
    leaderboard.show()

st.sidebar.write("🔹 Built with ❤️ using Streamlit")
