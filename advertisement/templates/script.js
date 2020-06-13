/*var app = angular.module('myApp', []);

app.controller('returnData', function($scope, $http) {	
	$scope.displayData = function(){
		$http.get("get_data")
		.success(function(data){
			console.log(data)
		});
	}
});*/

function getData(){
	fetch('http://get_data')
		.then(response => response.json())                                    	 
		.then(function (data) {
				console.log(data);
	})

			
}
function ajouter() {
	var i = 1;
	var cards = document.getElementById("Ctner");
	var newcard = document.createElement("div");
	newcard.className = "card";
	var newimg = document.createElement("img");
	newimg.className = "d-block w-100";
	newimg.src = "i130780-.jpeg";
	var newCrdBody = document.createElement("div");
	newCrdBody.className = "card-body";
	var newtitle = document.createElement("h4");
	newtitle.className = "card-title";
	newtitle.innerHTML = "Bouffe de type poulet";
	if (i)
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
	a.value = "#collapsecard7";
	newbtn.setAttributeNode(a);
	newbtn.className = "btn btn-dark";
	newbtn.innerHTML = "More";
	var newbtn2 = document.createElement("button");
	newbtn2.className = "btn btn-primary";
	newbtn2.type = "button";
	newbtn2.innerHTML = "Add Meal";
	newCrdBody.appendChild(newtitle);
	newCrdBody.appendChild(newbtn);
	newCrdBody.appendChild(newbtn2);
	var newcollapse = document.createElement("div");
	newcollapse.className = "collapse";
	newcollapse.id = "collapsecard7";
	var lst = document.createElement("ul");
	lst.className = "list-group list-group-flush";
	var lstelt;
	for (var i=0;i<3;i++)
	{
		lstelt = document.createElement("li");
		lstelt.className = "list-group-item";
		lstelt.innerHTML = "Element " + i;
		lst.appendChild(lstelt);
	}
	newcollapse.appendChild(lst);
	newcard.appendChild(newimg);
	newcard.appendChild(newCrdBody);
	newcard.appendChild(newcollapse);
	cards.appendChild(newcard);
	return false;
}