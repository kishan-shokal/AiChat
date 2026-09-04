import streamlit as st


def render_history():

    for message in st.session_state.chat_history:

        role = message["role"]

        avatar = (
            "👤"
            if role == "user"
            else "🤖"
        )

        with st.chat_message(
            role,
            avatar=avatar,
        ):
            st.markdown(
                message["content"]
            )


def add_message(role, content):

    st.session_state.chat_history.append(
        {
            "role": role,
            "content": content,
        }
    )


def stream_response(agent, query):

    answer = ""

    with st.chat_message(
        "assistant",
        avatar="🤖",
    ):

        placeholder = st.empty()

        response = agent.stream(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": query,
                    }
                ]
            },
            {
                "configurable": {
                    "thread_id":
                    st.session_state.thread_id
                }
            },
            stream_mode="messages",
        )

        for chunk, metadata in response:

            if hasattr(chunk, "content"):

                content = chunk.content

                if isinstance(content, str):

                    answer += content

                    placeholder.markdown(
                        answer + "▌"
                    )

        placeholder.markdown(answer)

    return answer