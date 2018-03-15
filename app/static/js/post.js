"use strict";
document.addEventListener('DOMContentLoaded', () => {
	
	const form = document.querySelector("#form");
	const error = err => { throw Error(err) };

	function handler(e) {
		e.preventDefault();
		const data = new FormData(this);
		const values = Array.from(data.entries()).reduce((obj, [name,value]) => {
			obj[name] = value;
			return obj;
		}, {});
		const json = JSON.stringify(values);
		
		Promise.resolve(function() {
			if (this.has("csrf_token") && this.get("title") != "" && this.get("content") != "") {
				return true;
			}
			return false;
		})
		.then(response => {
			return (response.call(data) && Request.post("/api/topic", {
				data: json,
				headers: [
					["X-Requested-With", "XMLHttpRequest"],
					["Content-Type", "application/json; charset=utf-8"]
				]
			})) || error("blank inputs")
		})
		.then(response => {
			window.alert(response.message)
			console.info(response.posted)
			return Promise.resolve(window.confirm("want to create another?"))
		}).then(response => {
			return (!response && (window.location = window.location.origin)) || ( window.location = window.location.href)
		})
		.catch(error => {
			window.alert(error.message)
			console.error(error)
		})
	}
	form.addEventListener("submit", handler.bind(form));
}, false);