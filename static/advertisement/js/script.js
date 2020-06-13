
window.onload = function() {
   	getData();
   }

function getData(){
	fetch('get_data')
		.then(response => response.json())                                    	 
		.then(function (data) {
				
			console.log(data);

		data.forEach(function(item, index, array){
			ajouter(item);
		});
	})

			
}


function redirection(uid){
	window.location = '/chat/convCreation?uuid='+uid;
}
function ajouter(item) {
	console.log(item);
	var i = 1;
	var cards = document.getElementById("Ctner");
	var newcard = document.createElement("div");
	newcard.className = "card";
	var newimg = document.createElement("img");
	newimg.className = "d-block w-100";
	newimg.src = item.data.ProductImageUrl;
	var newCrdBody = document.createElement("div");
	newCrdBody.className = "card-body";
	var newtitle = document.createElement("h4");
	newtitle.className = "card-title";
	newtitle.innerHTML = item.data.FoodTitle;
	if (item.data.VegStatue)
	{
		var vegan = document.createElement("i");
		vegan.className = "text-success fas fa-leaf";
		newtitle.appendChild(vegan);
	}
	var newbtn = document.createElement("button");
	var a = document.createAttribute("data-toggle");
	a.value = "collapse";
	newbtn.setAttributeNode(a);
	a= document.createAttribute("href");
	a.value = "#" + item.data.foodDescription;
	newbtn.setAttributeNode(a);
	newbtn.className = "btn btn-dark";
	newbtn.innerHTML = "More";
	var newbtn2 = document.createElement("button");
	newbtn2.className = "btn btn-primary";
	newbtn2.type = "button";
	newbtn2.innerHTML = "concact";
	var redirection_to_channel = document.createAttribute("onclick");
	redirection_to_channel.value = "redirection('"+item.id+"')";
	newbtn2.setAttributeNode(redirection_to_channel);
	newCrdBody.appendChild(newtitle);
	newCrdBody.appendChild(newbtn);
	newCrdBody.appendChild(newbtn2);
	var newcollapse = document.createElement("div");
	newcollapse.className = "collapse";
	newcollapse.id = item.data.foodDescription;
	var lst = document.createElement("ul");
	lst.className = "list-group list-group-flush";
	var lstelt;
	for (var i=0;i<3;i++)
	{
		lstelt = document.createElement("li");
		lstelt.className = "list-group-item";
		lstelt.innerHTML = "OK " + i;
		lst.appendChild(lstelt);
	}
	newcollapse.appendChild(lst);
	newcard.appendChild(newimg);
	newcard.appendChild(newCrdBody);
	newcard.appendChild(newcollapse);
	cards.appendChild(newcard);
	return false;
}