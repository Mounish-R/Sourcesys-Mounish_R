import streamlit as st
from gemini_api import load_gemini, get_response
from transformer_utils import analyze_input

# Title
st.title(" AI Chatbot")
st.subheader("Built with Gemini + Transformers")

# Load model once
model = load_gemini()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input (like ChatGPT)
user_input = st.chat_input("Type your message...")

if user_input:

    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # Transformer analysis
    sentiment = analyze_input(user_input)

    # Gemini response
    bot_response = get_response(model, user_input)

    # Store bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    with st.chat_message("assistant"):
        st.write(bot_response)
        st.caption(f"Sentiment: {sentiment['label']}")


