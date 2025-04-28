import streamlit as st
import asyncio

# Example dummy response function
async def ask_agent(prompt):
    return f"You said: {prompt[::-1]}"  # just reverses text for demo

# Title
st.title("💬 Fancy Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! Ask me anything."}
    ]

# Custom chat bubble styles
st.markdown(
    """
<style>
.chat-container {
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.chat-message {
    display: flex;
    width: 100%;
}
.chat-message.user {
    justify-content: flex-end;
}
.chat-message.assistant {
    justify-content: flex-start;
}
.bubble {
    padding: 10px 15px;
    border-radius: 15px;
    max-width: 70%;
    word-wrap: break-word;
}
.bubble.user {
    background-color: #dcf8c6;
    color: black;
}
.bubble.assistant {
    background-color: #f1f0f0;
    color: black;
}
</style>
<div class="chat-container">
    """, 
    unsafe_allow_html=True
)

# Display chat history
for msg in st.session_state.messages:
    role = msg["role"]
    content = msg["content"]
    st.markdown(f"""
    <div class="chat-message {role}">
        <div class="bubble {role}">{content}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Input box for user to type message
if prompt := st.chat_input("Type your message here..."):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user's message immediately
    st.markdown(f"""
    <div class="chat-message user">
        <div class="bubble user">{prompt}</div>
    </div>
    """, unsafe_allow_html=True)

    # Generate assistant reply (with context if needed)
    history = ''.join([f"{m['role']}: {m['content']}\n" for m in st.session_state.messages[-5:]])
    response = asyncio.run(ask_agent(history))

    # Append assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Display assistant response immediately
    st.markdown(f"""
    <div class="chat-message assistant">
        <div class="bubble assistant">{response}</div>
    </div>
    """, unsafe_allow_html=True)

