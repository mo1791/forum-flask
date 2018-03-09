const inputs = document.querySelectorAll(".form-control")

for (input of inputs) {
	input.classList.contains("is-invalid") && input.classList.remove("is-invalid")
	input.parentNode.classList.contains("has-danger") && input.parentNode.classList.remove("has-danger")
	if (null != (nextElement = input.nextElementSibling)) {
		input.parentNode.classList.add("has-danger")
		input.classList.add("is-invalid")
	}	
}
