import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Group Chat", layout="centered")
st.title("🌐 Shared Group Chat")

components.html("""
<div id="chatBox" style="height:300px;overflow-y:scroll;border:1px solid #ccc;padding:10px;margin-bottom:10px;"></div>
<input id="chatInput" type="text" placeholder="Type your message..." style="width:80%;padding:5px;" />
<button onclick="sendMessage()">Send</button>

<script>
const ws = new WebSocket("ws://localhost:8000/ws");

ws.onmessage = (event) => {
    const msg = JSON.parse(event.data);
    const chatBox = document.getElementById("chatBox");
    const p = document.createElement("p");
    p.textContent = msg.sender + ": " + msg.text;
    chatBox.appendChild(p);
    chatBox.scrollTop = chatBox.scrollHeight;
};

function sendMessage() {
    const input = document.getElementById("chatInput");
    if (input.value.trim() === "") return;
    const message = {
        sender: "User",
        text: input.value
    };
    ws.send(JSON.stringify(message));
    input.value = "";
}
</script>
""", height=400)

