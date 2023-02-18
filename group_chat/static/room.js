const roomName = JSON.parse(document.getElementById('room-name').textContent);
const chatSocket = new WebSocket("ws://" + window.location.host + '/ws/roomchat/' + roomName + '/');
const requestUser = JSON.parse(document.getElementById('request-user').textContent);
const timeNow = JSON.parse(document.getElementById('time-now').textContent);

chatSocket.onopen = function (e) {
    console.log("websocket connection successfull")
}
chatSocket.onclose = function (e) {
    console.log("websocket connection is disconnected")
}
chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data)
    var sendDiv = document.createElement("div").classList.add("d-flex","justify-content-end");
    var receiveDiv = document.createElement("div").classList.add("d-flex","justify-content-start");
    var p = document.createElement('p');
    console.log(data.username,requestUser)
    if (data.username == requestUser) {

        p.innerHTML = '<small>' + data.message + '</span>';
        sendDiv.appendChild(p)
        document.getElementById("message-box").appendChild(sendDiv)

    }else{
        p.innerHTML = '<span>' + data.username + '</span>' + '<br/>' + '<small>' + data.message + '</span>';
        receiveDiv.appendChild(p)
        document.getElementById("message-box").appendChild(receiveDiv)

    }
   
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