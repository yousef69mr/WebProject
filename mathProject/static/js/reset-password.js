const pass = document.querySelector('input[name="password"]')
const passwordmessage = document.querySelector('#password-error')
/*****************************************************/
const confirmPass = document.querySelector('input[name="confirmPassword"]')
const confirmPasswordMessage = document.querySelector('#confirmPassword-error')
/*****************************************************/

pass.addEventListener('input',(e)=>{
    
    if(e.target.value.length < 8){
        pass.classList.add('error')
        passwordmessage.textContent = "at least 8 characters"
        submitbtn.disabled = true;
        
    }else{
        pass.classList.remove('error')
        passwordmessage.textContent = ""
        submitbtn.disabled = false;
    }

    if(e.target.value !== confirmPass.value && confirmPass.value.length > 0){
        confirmPass.classList.add('error')
        confirmPasswordMessage.textContent = "passwords must match"
        submitbtn.disabled = true;
    }else{
        confirmPass.classList.remove('error')
        confirmPasswordMessage.textContent = ""
        submitbtn.disabled = false;
    }

});

confirmPass.addEventListener('input',(e)=>{
    if(e.target.value !== pass.value){
        confirmPass.classList.add('error')
        confirmPasswordMessage.textContent = "passwords must match"
        submitbtn.disabled = true;
    }else{
        confirmPass.classList.remove('error')
        confirmPasswordMessage.textContent = ""
        submitbtn.disabled = false;
    }
});





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
  

/* hide and visible of password */

function revealconfirmPassword(){
    
	var x=document.querySelector("input[name='confirmPassword']");
	var y=document.getElementById("hide3");
	var z=document.getElementById("hide4");
  
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