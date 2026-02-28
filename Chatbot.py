# from google.genai import  Client
# from google.genai import types
#

# print("WELCOME TO MENTAL HEALTH SUPPORT")
# print("I hope you are doing well today .Please tell me your thoughts(Type endchat to exit)")
#
# userinput=input("user: ")
# while userinput.lower()!= 'endchat':
#     systemoutput=client.models.generate_content(
#         contents= userinput,
#         model= 'gemini-2.5-flash-lite',
#         config= types.GenerateContentConfig(
#             system_instruction="You are a mental# health support agent.Answer in 1-10 line, within 2000 characters.Don't be over judgemental ,be little empathetic"
#         )
#     )
#     print("Chatbot: "+systemoutput.text)
#     userinput = input("user: ")
import streamlit as st
from google.genai import Client
from google.genai import types
import os

# Page config
st.set_page_config(page_title="Mental Health Support Chatbot", page_icon="🧠")

st.title("🧠 Mental Health Support Chatbot")
st.write("I hope you are doing well today. Share your thoughts below.")

# Load API key from Streamlit secrets
client = Client(api_key=st.secrets["GEMINI_API_KEY"])

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input box
user_input = st.chat_input("Type your message here...")

if user_input:
    # Show user message
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate response
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=user_input,
        config=types.GenerateContentConfig(
            system_instruction=(
                "You are a mental health support agent. "
                "Be empathetic, non-judgmental, and supportive. "
                "Keep responses between 1–10 lines."
            )
        ),
    )

    bot_reply = response.text

    # Show bot message
    st.chat_message("assistant").write(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})