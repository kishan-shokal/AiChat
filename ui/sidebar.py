import streamlit as st

from utils.session import new_chat


def render_sidebar():

    with st.sidebar:

        st.markdown("## 🤖 AI Web Agent")

        st.caption(
            "Groq + LangGraph + Google Search"
        )

        st.divider()

        if st.button(
            "＋ New conversation",
            use_container_width=True,
            type="primary",
        ):
            new_chat()
            st.rerun()

        st.divider()

        st.markdown("### Model")

        st.code(
            "openai/gpt-oss-20b",
            language="text",
        )

        st.markdown("### Tools")

        st.markdown(
            """
            🔎 Google Search  
            🧠 Conversation Memory  
            ⚡ Streaming
            """
        )

        st.divider()

        st.caption(
            f"Thread: {st.session_state.thread_id[:8]}"
        )