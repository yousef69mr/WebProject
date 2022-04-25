document.addEventListener("DOMContentLoaded", () => {
  let check = [false,false,false,false,false];
  document.querySelectorAll(".inp").forEach(input => {
      input.addEventListener('input', () => {

          if(input.classList.contains('usrname')){
              if(input.value.trim().length !== 0) {check[0]=true;}
              else{check[0] = false;}
          }
          if(input.classList.contains('phone')){
              if(input.value.trim().length !== 0) {check[1]=true;}
              else{check[1] = false;}
          }
          if(input.classList.contains('phone2')){
              if(input.value.trim().length !== 0) {check[2]=true;}
              else{check[2] = false;}
          }
          if(input.classList.contains('pswd')){
              /*document.querySelector('.cpswd').value = "";
              document.querySelector('.cpswd').parentElement.querySelector('span').innerText = "";
              check[4] = false;*/
              if(input.value.trim().length !== 0) {check[3]=true;}
              else{check[3] = false;}
          }
         /* if(input.classList.contains('cpswd')){
              if(input.value.trim().length !== 0) {
                  if(input.value !== document.querySelector('.pswd').value) {
                      input.parentElement.querySelector('span').innerText = "Password must match";
                      check[4] = false;
                  }
                  else {
                      input.parentElement.querySelector('span').innerText = "";
                      check[4]=true;
                  }
              }
              else{check[4] = false;}
          }*/
          if(input.classList.contains('email')){
              if(input.value.trim().length !== 0) {check[4]=true;}
              else{check[4] = false;}
          }

          let i;
          for(i=0;i<5;i++) {
              if(!check[i]) {
                  break;
              }
          }

          if(i===5) {
              document.querySelector('input[type="submit"]').disabled = false;
          }
          else {
              document.querySelector('input[type="submit"]').disabled = true;
          }

      });
  });
 
  
});


/*pop up Menu*/

 var c=0;

 function pop(){

    if(c==0){

        document.getElementById("box").style.display="block";
        c=1;
    }else {
        document.getElementById("box").style.display="none";
        c=0;
    }
}