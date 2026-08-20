# 🤖 AI Mood Chatbot

A simple AI chatbot built with **Python, LangChain, Mistral AI, and Streamlit**.

The interesting part of this project is that you can choose the chatbot's personality before starting the conversation:

* 😡 **Angry Mode**
* 😂 **Funny Mode**
* 😢 **Sad Mode**

The selected mood is passed to the AI as a **system prompt**, which changes the way it responds.

## 🛠️ Tech Used

* Python
* LangChain
* Mistral AI (`mistral-small-2506`)
* Streamlit

## ⚙️ How It Works

```text
Choose Mood
     ↓
System Prompt
     ↓
Mistral AI
     ↓
AI Response
```

The chatbot also keeps the conversation history during the session using LangChain's `HumanMessage`, `AIMessage`, and `SystemMessage`.

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Make sure your **Mistral API key** is configured before running the application.

## 🌐 Live Demo

👉 [Try AI Mood Chatbot](https://chatbot-2xnmhqcbk7fwdsxfzjddki.streamlit.app/)

## 🔮 Future Improvements

* Automatic mood detection
* More personalities
* Voice input/output
* Long-term conversation memory
* Better UI

## 👨‍💻 Author

**Raushan Kumar**
AI & Robotics Student | AI/ML & GenAI Enthusiast
