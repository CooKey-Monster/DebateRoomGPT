import streamlit as st
#from clientGemini import ask_agent, async_to_sync
import asyncio


st.title("💬 Debate")
st.caption("🚀 Are bananas vegetables?")
st.markdown(
    """
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        .stAppDeployButton {display:none;}
        footer {visibility: hidden;}
    </style>
""",
    unsafe_allow_html=True,
)

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]

#for msg in st.session_state.messages:
#    st.chat_message(msg["role"]).write(msg["content"])

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"""
            <div style='text-align: right; background-color: #dcf8c6; padding: 10px; border-radius: 10px; margin: 5px; display: inline-block; max-width: 80%;'>
                {msg["content"]}
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div style='text-align: left; background-color: #f1f0f0; padding: 10px; border-radius: 10px; margin: 5px; display: inline-block; max-width: 80%;'>
                {msg["content"]}
            </div>
            """,
            unsafe_allow_html=True,
        )


if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    history = ''.join([f"{m['role']}: {m['content']}\n" for m in st.session_state.messages[-5:]])
    #response = asyncio.run(ask_agent(prompt))
    #response = asyncio.run(ask_agent(history))
    #msg = response
    st.session_state.messages.append({"role": "assistant", "content": "nah, I'd win"})
    st.chat_message("assistant").write("nah id win")

