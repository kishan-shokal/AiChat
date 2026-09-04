import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        .block-container {
            max-width: 1100px;
            padding-top: 2rem;
            padding-bottom: 5rem;
        }

        .agent-title {
            font-size: 2rem;
            font-weight: 700;
        }

        .agent-subtitle {
            color: #888;
            margin-bottom: 2rem;
        }

        .welcome-card {
            padding: 2rem;
            border-radius: 16px;
            border: 1px solid rgba(128,128,128,0.2);
            background: rgba(128,128,128,0.04);
            margin: 2rem 0;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )