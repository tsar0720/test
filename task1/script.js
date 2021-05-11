let button = document.querySelector("button");

coinMas = ["<img src = ./img/1.png>", "<img src = ./img/2.png>"];


button.addEventListener("click", function() {
    document.getElementById("coin").innerHTML = coinMas[coinToss()];
});

function coinToss() {

    return Math.floor(Math.random() * 2);
  
}
  