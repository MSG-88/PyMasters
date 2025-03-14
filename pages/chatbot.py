import streamlit as st
from streamlit_chat import message  # For chat UI
import openai  # AI chatbot integration
import os


def show():
    st.title("🤖 AI Python Chatbot")
    openai.api_key = os.getenv("OPENAI_API_KEY")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    for msg in st.session_state["messages"]:
        message(msg["content"], is_user=msg["is_user"])

    user_input = st.text_input("Ask me anything about Python:")
    if user_input:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        bot_reply = response["choices"][0]["message"]["content"]
        st.session_state["messages"].append({"content": user_input, "is_user": True})
        st.session_state["messages"].append({"content": bot_reply, "is_user": False})
        message(bot_reply)
