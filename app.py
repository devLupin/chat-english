import streamlit as st
from streamlit_chat import message
import uuid
from whisper import get_whisper
from ocr import get_ocr
import os
import errno

st.set_page_config(
    page_title="Chat English",
    page_icon=":robot:"
)

st.header("Chat English")
st.markdown("Lupin - [github](https://github.com/devLupin/chat-english)")
st.markdown("")
st.markdown("")
st.markdown("A faster way to make perpect sentence in English.")
st.markdown("[Usage](https://github.com/devLupin/chat-english#usage)")
st.markdown("")
st.markdown("")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def remove(file):
    try:
        os.remove(file)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise

def get_text():
    st.markdown("\n\n")
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



image_file = st.file_uploader("Upload image for OCR", type=["png","jpg","jpeg"])
if image_file is not None:
    name = uuid.uuid4()
    f_name = "temp-" + str(name) + ".png"
    
    with open(f_name, "wb") as f:
        f.write((image_file).getbuffer())
    text = get_ocr(f_name)
    remove(f_name)
    
    st.markdown("#### OCR text : ")
    st.markdown(f"\n\n{text}")


user_input = get_text()

col1, col2, col3, col4 = st.columns(4)
with col1:
    grammar_btn = st.button(label="grammar")
with col2:
    naturally_btn = st.button(label="naturally")
with col3:
    easier_btn = st.button(label="easier")
with col4:
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