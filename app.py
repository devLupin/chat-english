import streamlit as st
from streamlit_chat import message
import requests
from whisper import get_whisper

st.set_page_config(
    page_title="Chat English - Demo",
    page_icon=":robot:"
)

st.header("Chat English - Demo")
st.markdown("[Github](https://github.com/devLupin/chat-english)")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("Enter your scripts: ","", key="input")
    return input_text 

def get_result(text, opt):
    res = get_whisper(text, opt)
    start_idx = 0
    for i, c in enumerate(res):
        if c != '\n':
            start_idx = i
            break
    
    return res[start_idx:]



user_input = get_text()
grammar_btn = st.button(label="grammar")
naturally_btn = st.button(label="naturally")
easier_btn = st.button(label="easier")
typo_btn = st.button(label="typo")

if user_input != "" and grammar_btn:
    st.session_state.past.append(user_input)
    
    res = get_result(user_input, "correct")
    st.session_state.generated.append(res)

elif user_input != "" and naturally_btn:
    st.session_state.past.append(user_input)
    
    res = get_result(user_input, "naturally")
    st.session_state.generated.append(res)

elif user_input != "" and easier_btn:
    st.session_state.past.append(user_input)
    
    res = get_result(user_input, "easier")
    st.session_state.generated.append(res)

elif user_input != "" and typo_btn:
    st.session_state.past.append(user_input)
    
    res = get_result(user_input, "typo")
    st.session_state.generated.append(res)

elif user_input:
    st.session_state.past.append(user_input)
    
    res = get_result(user_input, "correct")
    st.session_state.generated.append(res)


if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')