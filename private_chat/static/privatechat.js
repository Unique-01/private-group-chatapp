const userName = JSON.parse(document.getElementById("username").textContent);
const requestUser = JSON.parse(
  document.getElementById("request-user").textContent
);
const chatSocket = new WebSocket(
  "ws://" + window.location.host + "/ws/privatechat/" + userName + "/"
);

const timeNow = JSON.parse(document.getElementById("time-now").textContent);
var dateOptions = { hour: "numeric", minute: "numeric", hour12: true };
window.scrollTo(
  0,
  document.body.scrollHeight || document.documentElement.scrollHeight
);

let connStatus = document.getElementById("status");
connStatus.innerHTML = "Connecting";

chatSocket.onopen = function (e) {
  console.log("websocket connection successfull");
  connStatus.classList.add("text-success");
  connStatus.innerHTML = "Connected";
};

chatSocket.onclose = function (e) {
  console.log("websocket connection is disconnected");
  connStatus.classList.add("text-danger");
  connStatus.innerHTML = "Disconnected";
};

chatSocket.onmessage = function (e) {
  const data = JSON.parse(e.data);
  var sendDiv = document.createElement("div");
  sendDiv.classList.add("d-flex", "justify-content-end");
  var receiveDiv = document.createElement("div");
  receiveDiv.classList.add("d-flex", "justify-content-start");
  var sentMessage = document.createElement("p");
  sentMessage.classList.add(
    "ml-10",
    "send-bg",
    "p-2",
    "mb-3",
    "text-white",
    "rounded"
  );
  var receiveMessage = document.createElement("p");
  receiveMessage.classList.add(
    "mr-10",
    "mb-3",
    "p-2",
    "rounded",
    "receive-bg",
    "text-white"
  );
  var timestamp = new Date(data.timestamp).toLocaleString("en", dateOptions);
  sentMessage.innerHTML =
    "<span>" +
    data.message +
    "</span>" +
    "<br/>" +
    '<small class="d-flex justify-content-end timestamp">' +
    timestamp.toLowerCase() +
    "</small>";
  receiveMessage.innerHTML =
    "<span>" +
    data.message +
    "</span>" +
    "<br/>" +
    '<small class="timestamp">' +
    timestamp.toLowerCase() +
    "</small>";
  sendDiv.appendChild(sentMessage);
  receiveDiv.appendChild(receiveMessage);
  document.querySelector("#message-input").value = "";
  if (data.sender == requestUser) {
    document.getElementById("message-box").appendChild(sendDiv);
  } else {
    document.getElementById("message-box").appendChild(receiveDiv);
  }
  window.scrollTo(
    0,
    document.body.scrollHeight || document.documentElement.scrollHeight
  );
};

document.getElementById("message-input").focus();
document.getElementById("message-input").onkeyup = function (e) {
  if (e.keyCode == 13) {
    document.getElementById("message-submit").click();
  }
};

document.getElementById("message-submit").onclick = function (e) {
  var message = document.getElementById("message-input").value;
  chatSocket.send(
    JSON.stringify({
      message: message,
      sender: requestUser,
      timestamp: timeNow,
    })
  );
};
