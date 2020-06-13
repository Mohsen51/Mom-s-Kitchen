window.onload = function() {
   
    getData();
}


function getData(){
    fetch('/chat/get_conversations')
        .then(response => response.json())                                       
        .then(function (data) {
                
           

        data.forEach(function(item, index, array){
            console.log(item);
            getContact(item)
        });
    })

            
}


function getContact(data) {
    var list = document.querySelector(".msg-list");
    var div = document.createElement("div");
    div.className = "contact";
    var contact = document.createElement("a");
    contact.href = "convDisplayMessage?uuid="+data.uuid_conv;
   
    var contactName = document.createElement("span");
    contactName.innerText = data.Username ;
   
  
    contact.appendChild(contactName);
   
    div.appendChild(contact);
    list.appendChild(div);
}