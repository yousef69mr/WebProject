const cards = document.querySelectorAll(".post-module");

cards.forEach(card => {
	card.addEventListener('mouseover', () => card.classList.add("hover"));
	card.addEventListener('mouseleave', () => card.classList.remove("hover"));
});
