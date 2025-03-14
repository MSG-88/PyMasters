import streamlit as st


def show():
    st.title("📚 Python Knowledge Hub")
    st.write("Explore Python tutorials, snippets, and best practices.")
    code_example = """
    def greet(name):
        return f"Hello, {name}! Welcome to PyMasters!"

    print(greet("Pythonista"))
    """
    st.code(code_example, language='python')
