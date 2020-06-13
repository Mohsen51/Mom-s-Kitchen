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
    contact.href = "convDisplayMessage?uid="+data.uuid_conv;
    var image = document.createElement("img");
    image.src = "../Main page/i130780-.jpeg";
    var contactName = document.createElement("span");
    contactName.innerText = data.Username + ":";
    var plate = document.createElement("span");
    plate.textContent = "Poulet";
    contact.appendChild(image);
    contact.appendChild(contactName);
    contact.appendChild(plate);
    div.appendChild(contact);
    list.appendChild(div);
}