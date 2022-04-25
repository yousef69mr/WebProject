
var delayInMilliseconds = 900; //1 second

setTimeout(function() {
  //your code to be executed after 1 second
  document.querySelector(".waves").hidden = false;
  document.querySelector(".form").hidden = false;
}, delayInMilliseconds);



window.addEventListener("load",function(){
    const loader = document.querySelector(".loader");
    loader.className += " hidden";
    
});