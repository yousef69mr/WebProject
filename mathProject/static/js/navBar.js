// Select The Elements
var toggle_btn;
var big_wrapper;
var ScrollToTop_btn;
var hamburger_menu;
var overlay;
var bar;

function declare() {
  toggle_btn = document.querySelector(".toggle-btn");
  big_wrapper = document.querySelector(".big-wrapper");
  hamburger_menu = document.querySelector(".hamburger-menu");
  bar = document.querySelector(".bar");
  ScrollToTop_btn = document.querySelector("#btnScrollToTop");
  overlay = document.querySelector(".overlay");
}

const main = document.querySelector("main");

declare();

let dark = false;

function toggleAnimation() {
  // Clone the wrapper
  dark = !dark;
  let clone = big_wrapper.cloneNode(true);
  if (dark) {
    clone.classList.remove("light");
    clone.classList.add("dark");
  } else {
    clone.classList.remove("dark");
    clone.classList.add("light");
  }
  clone.classList.add("copy");
  main.appendChild(clone);

  document.body.classList.add("stop-scrolling");

  clone.addEventListener("animationend", () => {
    document.body.classList.remove("stop-scrolling");
    big_wrapper.remove();
    clone.classList.remove("copy");
    // Reset Variables
    declare();
    events();
  });
}

function events() {

  
  toggle_btn.addEventListener("click", toggleAnimation);
  
  hamburger_menu.addEventListener("click", () => {
    big_wrapper.classList.toggle("active");
  });

  
  ScrollToTop_btn.addEventListener("click",function(){

    //window.scrollTo(0,0);

    /*window.scrollTo({
        top:0,
        left:0,
        behavior:"smooth"
    });
    */
   $("html,body").animate({scrollTop:0},"slow");
  });
}

events();

