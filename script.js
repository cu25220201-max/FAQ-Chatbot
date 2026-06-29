
const chatBox = document.getElementById("chat-box");
const inputBox = document.getElementById("question");
const sendButton = document.getElementById("send-btn");
const themeBtn = document.getElementById("themeBtn");
const historyBox = document.getElementById("historyList");


window.addEventListener("load", function () {

    loadChat();
    loadHistory();
    scrollBottom();
});


async function sendMessage() {

    const question = inputBox.value.trim();

    if (question === "") {
        alert("Please enter a question.");
        return;
    }

    addUserMessage(question);
    saveChatTitle(question);

    inputBox.value = "";

    showTyping();

    try {

        const response = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question })
        });

        const data = await response.json();

        hideTyping();

        addBotMessage(data.answer, data.confidence);

    } catch (error) {

        hideTyping();
        addBotMessage("Server Error! Please try again.", 0);

        console.error(error);
    }
}


function addUserMessage(message) {

    const div = document.createElement("div");
    div.className = "user-message";
    div.innerHTML = "<strong>You:</strong><br>" + message;

    chatBox.appendChild(div);

    saveChat();
    scrollBottom();
}


function addBotMessage(answer, confidence) {

    const div = document.createElement("div");
    div.className = "bot-message";

    div.innerHTML = `
        <strong>Bot:</strong><br>
        ${answer}
        <br><br>
        <small>Confidence: ${(confidence * 100).toFixed(0)}%</small>
    `;

    chatBox.appendChild(div);

    saveChat();
    scrollBottom();
}


function showTyping() {

    if (!document.getElementById("typing")) {

        const typing = document.createElement("div");
        typing.className = "typing";
        typing.id = "typing";
        typing.innerHTML = "🤖 Bot is typing...";

        chatBox.appendChild(typing);
        scrollBottom();
    }
}

function hideTyping() {
    const typing = document.getElementById("typing");
    if (typing) typing.remove();
}


function saveChat() {
    localStorage.setItem("chat", chatBox.innerHTML);
}


function loadChat() {
    const oldChat = localStorage.getItem("chat");
    if (oldChat) {
        chatBox.innerHTML = oldChat;
    }
}


function scrollBottom() {
    chatBox.scrollTop = chatBox.scrollHeight;
}


function saveChatTitle(question) {

    let history = JSON.parse(localStorage.getItem("historyList")) || [];

    history.push(question);

    localStorage.setItem("historyList", JSON.stringify(history));

    loadHistory();
}


function loadHistory() {

    let history = JSON.parse(localStorage.getItem("historyList")) || [];

    historyBox.innerHTML = "";

    history.forEach((item) => {

        let div = document.createElement("div");

        div.innerText = item;

        div.onclick = () => {
            alert("Load chat: " + item);
        };

        historyBox.appendChild(div);
    });
}


sendButton.addEventListener("click", sendMessage);

inputBox.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});


themeBtn.onclick = function () {

    document.body.classList.toggle("dark");

    themeBtn.innerHTML = document.body.classList.contains("dark")
        ? "☀️"
        : "🌙";
};