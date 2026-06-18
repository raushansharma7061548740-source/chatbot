from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

st.set_page_config(
    page_title="AI Mood Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Mood Chatbot")
st.write("Choose AI mode from frontend and start chatting.")

model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9
)

mode_choice = st.selectbox(
    "Choose your AI model mode:",
    ["Angry Mode 😡", "Funny Mode 😂", "Sad Mode 😢"]
)

if mode_choice == "Angry Mode 😡":
    mode = "You are an angry AI agent"
elif mode_choice == "Funny Mode 😂":
    mode = "You are a funny AI agent"
else:
    mode = "You are a sad AI agent"

if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content=mode)]

if "current_mode" not in st.session_state:
    st.session_state.current_mode = mode_choice

if st.session_state.current_mode != mode_choice:
    st.session_state.messages = [SystemMessage(content=mode)]
    st.session_state.current_mode = mode_choice
    st.rerun()

for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))

    with st.chat_message("user"):
        st.write(user_input)

    response = model.invoke(st.session_state.messages)

    st.session_state.messages.append(AIMessage(content=response.content))

    with st.chat_message("assistant"):
        st.write(response.content)