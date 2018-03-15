"use strict";
document.addEventListener('DOMContentLoaded', () => {
	
	const form = document.querySelector("#form");
	function handler(e) {
		e.preventDefault();
		const data = new FormData(this);
		const values = Array.from(data.entries()).reduce((obj, [name,value]) => {
			obj[name] = value;
			return obj;
		}, {});
		const json = JSON.stringify(values);
		Request.post("/api/topic", {
			data: json,
			headers: [
				["X-Requested-With", "XMLHttpRequest"],
				["Content-Type", "application/json; charset=utf-8"]
			]
		})
		.then(response => {
			console.info(response)
		})
		.catch(error => {
			console.error(error.message)
		})
	}
	form.addEventListener("submit", handler.bind(form));
}, false);