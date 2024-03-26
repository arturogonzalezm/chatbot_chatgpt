import datetime

import streamlit as st

from backend.chatgpt import get_gpt_response
from frontend.css.css import custom_css


def write_prompt():
    st.title(':blue[Streamlit Chatbot]')
    # Ensure 'history' and 'conversations' are initialized
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'conversations' not in st.session_state:
        st.session_state.conversations = []

    # Function to save the current conversation if it's not already saved
    def save_current_chat():
        if st.session_state.history:
            chat_content = "\n".join(st.session_state.history)
            # Check if this conversation is already saved
            if not any(conversation['content'] == chat_content for conversation in st.session_state.conversations):
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                st.session_state.conversations.append(
                    {"name": f"Conversation from {timestamp}", "content": chat_content})
                st.sidebar.success('✅ Conversation saved!')
            else:
                st.sidebar.info('ℹ️ This conversation is already saved.')

            # Clear current chat history after checking
            st.session_state.history = []

    # Sidebar controls for conversation management
    if st.sidebar.button('🆕 New Conversation'):
        save_current_chat()  # Check, save, and then clear the chat before starting a new one

    if st.sidebar.button('💾 Save Conversation'):
        save_current_chat()

    # Display and manage saved conversations in the sidebar
    st.sidebar.write("🗂 Saved Conversations:")
    for index, conversation in enumerate(st.session_state.conversations):
        new_name = st.sidebar.text_input(f"📝 Rename '{conversation['name']}'",
                                         value=conversation['name'],
                                         key=f"name_{index}")
        if new_name != conversation['name']:
            st.session_state.conversations[index]['name'] = new_name

        if st.sidebar.button(f"📂 Load '{conversation['name']}'", key=f"load_{index}"):
            st.session_state.history = conversation['content'].split('\n')

    # Chat input form
    with st.form(key='chat_form'):
        user_input = st.text_input("Write your message here...", key="user_input")
        submit_button = st.form_submit_button(label='📩')

    # Process form submission
    if submit_button and user_input:
        st.session_state.history.append(f"You: {user_input}")
        gpt_response = get_gpt_response(user_input)
        st.session_state.history.append(f"GPT: {gpt_response}")

    st.markdown(custom_css, unsafe_allow_html=True)
    st.text_area("Conversation:", value="\n".join(st.session_state.history), height=400, key="conversation")
