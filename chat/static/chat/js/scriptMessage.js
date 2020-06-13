window.onload = function() {
    getContact();
    getData();
}

function keyCode(event) {
    var x = event.keyCode;
    if (x == 13) {
        document.getElementById("btn").click();
    }
}

function addReceived(user,message,userOwner) {
    console.log(message);
    console.log(user);
    console.log(userOwner);
   
    //select chat DOM
	var msg = document.querySelector(".msg-page");

    //create new message container
    var newChat = document.createElement("div");
	var newMsg = document.createElement("div");

    //check who is the owner of the message 
    if(user!=info.user_name){
        newChat.className = "received-chats";
    	newMsg.className = "received-msg";
    }
    else{
        newChat.className = "sent-chats";
        newMsg.className = "sent-msg";
    }
    var newText = document.createElement("p");
    newText.innerText = message;

    //add to the DOM
    newMsg.appendChild(newText);
    newChat.appendChild(newMsg);
    msg.appendChild(newChat);
}

function getContact() {
    var header = document.querySelector(".msg-header");
    var div = document.createElement("div");
    div.className = "active";
    var contactName = document.createElement("h4");
    contactName.textContent = "Contact";
    div.appendChild(contactName);
    header.appendChild(div);
}

function getData(){
    fetch('/chat/get_conversations')
        .then(response => response.json())                                       
        .then(function (data) {
                
            console.log(data);

        data.forEach(function(item, index, array){
            
        });
    })

            
}
