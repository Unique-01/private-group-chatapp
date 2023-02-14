const userName = JSON.parse(document.getElementById('username').textContent);
const requestUser = JSON.parse(document.getElementById('request-user').textContent);
const chatSocket = new WebSocket('ws://' + window.location.host + '/ws/privatechat/' + userName + '/');

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data)
    var div = document.createElement("div");
    div.innerHTML = data.sender + '<br/>' + data.message
    document.getElementById('message-input').value = "";

    document.getElementById("message-box").appendChild(div)
}

document.getElementById('message-submit').onclick = function (e) {
    var message = document.getElementById('message-input').value;
    chatSocket.send(JSON.stringify({ message: message, sender: requestUser }))
}