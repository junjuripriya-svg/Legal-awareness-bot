async function sendMessage() {

    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const message = input.value;

    if (!message) return;

    chatBox.innerHTML += `
        <div class="user">
            <b>You:</b> ${message}
        </div>
    `;

    input.value = "";

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    });

    const data = await response.json();

    chatBox.innerHTML += `
        <div class="bot">
           <b>LegalLens:</b><br>
        ${data.reply.replace(/\n/g, "<br>")}
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;
}
document.getElementById("user-input")
.addEventListener("keypress", function(event){

    if(event.key === "Enter"){
        sendMessage();
    }

});
function fillQuestion(question){
    document.getElementById("user-input").value = question;
}