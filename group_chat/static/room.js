const roomName = JSON.parse(document.getElementById('room-name').textContent);
const chatSocket = new WebSocket("ws://" + window.location.host + '/ws/roomchat/' + roomName + '/');
const requestUser = JSON.parse(document.getElementById('request-user').textContent);

chatSocket.onopen = function (e) {
    console.log("websocket connection successfull")
}
chatSocket.onclose = function (e) {
    console.log("websocket connection is disconnected")
}
chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data)
    var div = document.createElement("div");
    div.innerHTML = data.username + '<br/>' + data.message
    document.getElementById('message-input').value = "";

    document.getElementById("message-box").appendChild(div)
}
document.getElementById('message-input').focus();
document.getElementById('message-input').onkeyup = function (e) {
    if (e.keyCode == 13) {
        document.getElementById('message-submit').click();
    }
}
document.getElementById('message-submit').onclick = function (e) {
    var message = document.getElementById('message-input').value;
    chatSocket.send(JSON.stringify({ message: message, username: requestUser }))
}