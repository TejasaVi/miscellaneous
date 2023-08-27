const button = document.getElementById("theButton")
const data = document.getElementById("info")

const cars = [
		{ "make":"Porsche", "model":"911S" },
		{ "make":"Mercedes-Benz", "model":"220SE" },
		{ "make":"Jaguar","model": "Mark VII" }
	];

button.onclick= function(){

fetch("http://127.0.0.1:9000/receiver").then((response) => response.json()).then((data) => console.log(data));
}

