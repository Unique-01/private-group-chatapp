
const chatSocket = new WebSocket("ws://" + window.location.host + '/')

chatSocket.onopen = function (e) {
    console.log("websocket connection successfull")
}