import streamlit as st

from backend.chatgpt import get_gpt_response


def write_prompt():
    # Ensure 'history' is initialized
    if 'history' not in st.session_state:
        st.session_state.history = []

    # Define a form for the chat input
    with st.form(key='chat_form'):
        # Create a text input inside the form
        user_input = st.text_input("Write your message here...", key="user_input")
        # Create a submit button for the form
        submit_button = st.form_submit_button(label='Send')

    # If the form is submitted (which also resets the input field)
    if submit_button and user_input:
        # Add user message to the history
        st.session_state.history.append(f"You: {user_input}")
        # Get the response from GPT
        gpt_response = get_gpt_response(user_input)
        # Add GPT response to the history
        st.session_state.history.append(f"GPT: {gpt_response}")

    # Display the conversation history outside the form
    st.text_area("Conversation:", value="\n".join(st.session_state.history), height=300, key="conversation")
