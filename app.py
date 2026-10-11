
import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Chatbot knowledge base
responses = {
    "hello": "Hello! 👋 How can I help you today?",
    "hi": "Hi there! Welcome to my AI Chatbot.",
    "hey": "Hey! What would you like to know?",
    "your name": "I am Mahesh, your chatbot assistant.",
    "who are you": "I am Mahesh, a chatbot built using Python and Streamlit.",
    "python": "Python is a popular programming language used in AI, ML, automation, and web development.",
    "machine learning": "Machine Learning enables computers to learn patterns from data.",
    "artificial intelligence": "Artificial Intelligence helps machines perform tasks that normally require human intelligence.",
    "ai": "AI stands for Artificial Intelligence.",
    "help": "You can ask me about Python, AI, machine learning, or general greetings.",
    "thank": "You're welcome! 😊 Happy to help.",
    "bye": "Goodbye! 👋 Have a wonderful day.",
    "time": f"The current system time is {datetime.now().strftime('%I:%M %p')}.",
    "date": f"Today's date is {datetime.now().strftime('%d-%m-%Y')}."
}


def get_response(user_message):
    """Generate a response using basic keyword matching."""
    message = user_message.lower().strip()

    # Find matching keywords
    for keyword, response in responses.items():
        if keyword in message:
            return response

    return (
        "I'm still learning! 🤔 "
        "Try asking me about Python, AI, machine learning, "
        "or type 'help' to see what I can answer."
    )


# Application interface
st.title("🤖 Mahesh K - AI Chatbot")
st.caption("A simple chatbot built with Python and Streamlit")

st.markdown(
    "Hello! I'm Mahesh. Ask me a question to get started."
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! 👋 I'm Mahesh. How can I help you?"
        }
    ]

# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Chat cleared! What would you like to ask?"
        }
    ]
    st.rerun()

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Display and save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Generate and save chatbot response
    bot_response = get_response(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_response}
    )

    # Refresh the interface
    st.rerun()