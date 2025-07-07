import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini 1.5 Flash model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI setup
st.set_page_config(page_title="Gemini 1.5 Chatbot 💬", page_icon="🤖")
st.title("💬 Chat with Gemini 1.5 Flash")
st.markdown("Ask anything below:")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Say something...")

if prompt:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Gemini response
    with st.chat_message("assistant"):
        response = model.generate_content([prompt])
        st.markdown(response.text)

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": response.text})
