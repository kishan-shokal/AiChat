from dotenv import load_dotenv

load_dotenv()

import streamlit as st

from agent.agent import get_agent
from ui.styles import load_css
from ui.sidebar import render_sidebar
from ui.chat import (
    render_history,
    add_message,
    stream_response,
)
from utils.session import initialize_session


# =========================================================
# CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Web Agent",
    page_icon="🤖",
    layout="wide",
)


# =========================================================
# INITIALIZE
# =========================================================

initialize_session()

load_css()

render_sidebar()

agent = get_agent()


# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
    <div class="agent-title">
        🤖 AI Web Agent
    </div>

    <div class="agent-subtitle">
        Search the web. Think. Answer.
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# EMPTY STATE
# =========================================================

if not st.session_state.chat_history:

    st.markdown(
        """
        <div class="welcome-card">

        <h3>👋 What can I help you with?</h3>

        <p>
        Ask me anything. I can search the web
        and provide current information.
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# CHAT HISTORY
# =========================================================

render_history()


# =========================================================
# CHAT INPUT
# =========================================================

query = st.chat_input(
    "Ask anything..."
)


# =========================================================
# PROCESS QUERY
# =========================================================

if query:

    with st.chat_message(
        "user",
        avatar="👤",
    ):
        st.markdown(query)

    add_message(
        "user",
        query,
    )

    try:

        answer = stream_response(
            agent,
            query,
        )

        add_message(
            "assistant",
            answer,
        )

    except Exception as e:

        st.error(
            f"Something went wrong: {e}"
        )