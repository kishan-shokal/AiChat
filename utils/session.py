import uuid
import streamlit as st


def initialize_session():

    if "thread_id" not in st.session_state:
        st.session_state.thread_id = str(uuid.uuid4())

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


def new_chat():

    st.session_state.thread_id = str(uuid.uuid4())

    st.session_state.chat_history = []