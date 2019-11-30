window.onload = function() {

var teslaModels = [
        {
            "model": "modelS",
            "name": "Model S",
            "price": 69200,
            "year": 2016
        },
        {
            "model": "modelX",
            "name": "Model X",
            "price": 83700,
            "year": 2017
        },
        {
            "model": "model3",
            "name": "Model 3",
            "price": 35000,
            "year": 2017
        },
    ];
    

teslaModels.forEach(fucntion(item,index) {
	listE = document.createElement("th")
	listE.id = item.model
	listE.innerHTML = item.name
	document.getElementById("menu").appendChild(listE)
	})
	
teslaModels.forEach(mouseoverhandler);
function mouseoverhandler(item, index) {
	var elem = document.getElementById(item.model);
        elem.onmouseover = function(){
             var details = item;
            // if found, update DOM with information from array
            if(details!=null)
            {
                document.getElementById("data-table").removeAttribute('hidden');
                document.getElementById("model").innerHTML = details.name;
                document.getElementById("picture").innerHTML = '<img src="img/'+details.model+'.jpeg"/>';
                document.getElementById("price").innerHTML = "$"+details.price;
                document.getElementById("year").innerHTML = details.year;

            }
        }
}
