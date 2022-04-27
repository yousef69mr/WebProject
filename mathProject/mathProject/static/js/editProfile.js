const editbtn = document.querySelector('#edit-btn')
/*****************************************************/
const fname = document.querySelector('input[name="f-name"]')
const fnamemessage = document.querySelector('#fname-error')
/*****************************************************/
const lname = document.querySelector('input[name="l-name"]')
const lnamemessage = document.querySelector('#lname-error')
/*****************************************************/
const pass = document.querySelector('input[name="password"]')
const passwordmessage = document.querySelector('#password-error')
/*****************************************************/
const confirmPass = document.querySelector('input[name="confirmPassword"]')
const confirmPasswordMessage = document.querySelector('#confirmPassword-error')
/*****************************************************/
const gender = document.querySelector('select[name="gender"]')
const gendermessage = document.querySelector('#gender-error')
/*****************************************************/
const email = document.querySelector('input[name="email"]')
const emailmessage = document.querySelector('#email-error')
/*****************************************************/
const phone = document.querySelector('input[name="phone"]')
const phonemessage = document.querySelector('#phone-error')
/*****************************************************/
const parentPhone = document.querySelector('input[name="parentPhone"]')
const parentPhonemessage = document.querySelector('#parentPhone-error')
/*****************************************************/
const level = document.querySelector('select[name="level"]')
const levelmessage = document.querySelector('#level-error')
/*****************************************************/
const address = document.querySelector('.textarea')
const addressmessage = document.querySelector('#address-error')
/*****************************************************/
const submitbtn = document.querySelector('.submit-btn')
/*****************************************************/
const form = document.querySelector(".form");
const inputElements = form.querySelectorAll("input, select, checkbox, textarea");

var first = 0;

editbtn.addEventListener('click',()=>{
    if(first == 0){
        
        for(var key in inputElements){
            inputElements[key].disabled = false;
        }
        first = 1; 

    }else{
        for(var key in inputElements){
            inputElements[key].disabled = true;
        }
        first = 0; 
    }
});

console.log(editbtn)

fname.addEventListener('input',(e)=>{
    if(e.target.value.length < 8){
        fname.classList.add('error')
        fnamemessage.textContent = "name must be longer"
        //submitbtn.disabled = true;
    }else{
        fname.classList.remove('error')
        fnamemessage.textContent = ""
        //submitbtn.disabled = false;

    }
});


lname.addEventListener('input',(e)=>{
    if(e.target.value.length < 8){
        lname.classList.add('error')
        lnamemessage.textContent = "name must be longer"
        //submitbtn.disabled = true;
    }else{
        lname.classList.remove('error')
        lnamemessage.textContent = ""
        //submitbtn.disabled = false;
    }
});


pass.addEventListener('input',(e)=>{
    
    if(e.target.value.length < 8){
        pass.classList.add('error')
        passwordmessage.textContent = "at least 8 characters"
        //submitbtn.disabled = true;
        
    }else{
        pass.classList.remove('error')
        passwordmessage.textContent = ""
        //submitbtn.disabled = false;
    }

    if(e.target.value !== confirmPass.value && confirmPass.value.length > 0){
        confirmPass.classList.add('error')
        confirmPasswordMessage.textContent = "passwords must match"
        //submitbtn.disabled = true;
    }else{
        confirmPass.classList.remove('error')
        confirmPasswordMessage.textContent = ""
        //submitbtn.disabled = false;
    }

});

confirmPass.addEventListener('input',(e)=>{
    if(e.target.value !== pass.value){
        confirmPass.classList.add('error')
        confirmPasswordMessage.textContent = "passwords must match"
        //submitbtn.disabled = true;
    }else{
        confirmPass.classList.remove('error')
        confirmPasswordMessage.textContent = ""
        //submitbtn.disabled = false;
    }
});


gender.addEventListener('change',(e)=>{
    if(gender.value == ""){
        gender.classList.add('error')
        gendermessage.textContent = "This field is required"
        //submitbtn.disabled = true;
    }else{
        gender.classList.remove('error')
        gendermessage.textContent = ""
        //submitbtn.disabled = false;
    }
});


email.addEventListener('input',(e)=>{
    if(!e.target.value.includes('@') || !e.target.value.includes('.')){
        email.classList.add('error')
        emailmessage.textContent = "invalid email format"
        //submitbtn.disabled = true;
    }else{
        email.classList.remove('error')
        emailmessage.textContent = ""
        //submitbtn.disabled = false;
    }
});

phone.addEventListener('input',(e)=>{
    console.log(Math.floor(e.target.value));
    if(e.target.value.length != 11 || isNaN(e.target.value)){
        phone.classList.add('error')
        phonemessage.textContent = "invalid Format  (11 numbers !)"
        //submitbtn.disabled = true;
    }else{
        phone.classList.remove('error')
        phonemessage.textContent = ""
        //submitbtn.disabled = false;
    }
});


parentPhone.addEventListener('input',(e)=>{
    if(e.target.value.length != 11 || isNaN(e.target.value)){
        parentPhone.classList.add('error')
        parentPhonemessage.textContent = "invalid Format  (11 numbers !)"
        //submitbtn.disabled = true;
    }else{
        parentPhone.classList.remove('error')
        parentPhonemessage.textContent = ""
        //submitbtn.disabled = false;
    }
});


level.addEventListener('change',()=>{
    if(this.value == ""){
        level.classList.add('error')
        levelmessage.textContent = "This field is required"
        //submitbtn.disabled = true;
    }else{
        level.classList.remove('error')
        levelmessage.textContent = ""
        //submitbtn.disabled = false;
    }
});

address.addEventListener('change',(e)=>{
    if(e.target.value.length < 4){
        address.classList.add('error')
        addressmessage.textContent = "more than 4 characters"
        
    }else{
        address.classList.remove('error')
        addressmessage.textContent = ""
        
    }
});



$(document).ready(function(){
    setInterval(()=>{
        $.ajax({

            type :'GET',
            url : "/getStudents",
            success: function(response){
                
                for(var key in response.students){
                    if(response.students[key].email.toLowerCase() === email.value.toLowerCase()){
                        //console.log(response.students[key]);
                        email.classList.add('error');
                        emailmessage.textContent = "This Email already exists";
                    }else if(response.students[key].phone === phone.value){
                        phone.classList.add('error');
                        phonemessage.textContent= "This Phone Number is used before ";
                        //console.log(response.students[key]);
                    }
                }
                console.log(response.students)
            },
            error: function(response){
                alert("An Error Occured");
            }

        });

        submitbtn.disabled = false;
        

        //console.log(inputElements);

        for(var key in inputElements){
            if(inputElements[key].classList.contains('error')){
                submitbtn.disabled = true;
                break;
            }
        }


    },3000);
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