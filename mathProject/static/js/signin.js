

/* hide and visible of password */

function revealPassword(){
	var x=document.querySelector("input[name='password']");
	var y=document.getElementById("hide1");
	var z=document.getElementById("hide2");
  
	if(x.type==='password'){
	  x.type="text";
	  y.style.display="block";
	  z.style.display="none";
  
	}else{
  
	  x.type="password";
	  y.style.display="none";
	  z.style.display="block";
  
	}
}
  