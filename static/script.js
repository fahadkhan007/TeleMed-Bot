function sendMsg() {
    const input = document.getElementById("userInput");
    const msg = input.value.trim();
    if (!msg) return;
  
    // Show user's msg
    const chatbox = document.getElementById("chatbox");
    chatbox.innerHTML += `<div class="user-msg">${msg}</div>`;
    input.value = "";
  
    // Send to backend
    fetch("/get", {
      method: "POST",
      body: JSON.stringify({ msg: msg }),
      headers: { "Content-Type": "application/json" }
    })
      .then(res => res.json())
      .then(data => {
        chatbox.innerHTML += `<div class="bot-msg">${data.reply.replace(/\n/g, "<br>")}</div>`;
        chatbox.scrollTop = chatbox.scrollHeight;
      });
  }
  