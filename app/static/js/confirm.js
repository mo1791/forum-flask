const btns = document.querySelectorAll(".delete")

function handle(e) {
	e.preventDefault();
	if (window.confirm("are you sure that you want delete this topic")) {
		window.location = this.firstElementChild.pathname
	}
}
for (btn of btns) {
	btn.addEventListener("click", handle.bind(btn))
}