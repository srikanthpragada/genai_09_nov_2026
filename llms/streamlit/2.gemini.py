# streamlit run 2.gemini.py

import streamlit as st
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage

model = init_chat_model("gemini-3.5-flash-lite", model_provider="google_genai")

st.title("Get Answers from Gemini!")


# display textbox
prompt = st.text_input("Enter your prompt", "")
if len(prompt) > 0:
    response = model.invoke([SystemMessage(content="Give one line answer"),
                             HumanMessage(content = prompt)])
    st.write(response.content[0]['text'], unsafe_allow_html=True)

        