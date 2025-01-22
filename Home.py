import streamlit as st
from dotenv import load_dotenv

load_dotenv()
# Main page
st.set_page_config(page_title="Streamlit Multi-Page App")

st.title("Welcome to the Fractarium")
st.write("Auto PR Agent[WIP]: This is a tool that helps you to automate the process of creating a pull request.\n\n")
st.write("About Me: The RAG chatbot that introduces me")