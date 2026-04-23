const API = "http://127.0.0.1:8000";

function addMessage(text, type) {
    const chat = document.getElementById("chat-box");

    const msg = document.createElement("div");
    msg.className = "message " + type;
    msg.innerText = text;

    chat.appendChild(msg);
    chat.scrollTop = chat.scrollHeight;
}

// Upload Resume
async function upload() {
    const file = document.getElementById("file").files[0];
    if (!file) return alert("Select a file");

    let formData = new FormData();
    formData.append("file", file);

    addMessage("Uploading resume...", "bot");

    let res = await fetch(API + "/upload/", {
        method: "POST",
        body: formData
    });

    let data = await res.json();

    if (data.message) {
        addMessage("Resume uploaded successfully ✅", "bot");
    } else {
        addMessage("Error: " + data.error, "bot");
    }
}

// Generate Questions
async function getQuestions() {
    addMessage("Generating questions...", "bot");

    let res = await fetch(API + "/questions/");
    let data = await res.json();

    if (data.result) {
        addMessage(data.result, "bot");
    } else {
        addMessage("Error: " + data.error, "bot");
    }
}