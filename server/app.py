from typing import Literal

import streamlit as st
from pydantic import BaseModel

from llm import ask_question
from guardrails import is_question_allowed


class Message(BaseModel):
    """Message model."""
    role: Literal["user", "assistant"]
    content: str


def show_message(message: Message):
    """Show message in the message history.

    Args:
        message (Message): message to show
    """
    with st.chat_message(message.role):
        st.write(message.content)


def main():
    """Streamlit entrypoint."""
    st.title("Main")

    # Initialise messages
    if "messages" not in st.session_state:
        st.session_state.messages = [
            Message(
                role="assistant",
                content="How may I help you?"
            )
        ]

    for message in st.session_state.messages:
        show_message(message)

    question = st.chat_input()
    if question:
        st.session_state.messages.append(
            Message(
                role="user",
                content=question
            )
        )
        show_message(st.session_state.messages[-1])

        guardrails_decision = is_question_allowed(question)
        print(guardrails_decision)
        if guardrails_decision.overall_decision:
            response = ask_question(question)
            if guardrails_decision.has_passphrase:
                response = f"[PASSPHRASE USED] {response}"
        else:
            response = "Sneaky! Not answering that though."

        st.session_state.messages.append(
            Message(
                role="assistant",
                content=response
            )
        )
        show_message(st.session_state.messages[-1])


if __name__ == "__main__":
    main()
