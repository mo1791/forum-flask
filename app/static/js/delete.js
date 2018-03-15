const btns = document.querySelectorAll(".delete")
const error = err => { throw Error(err) }


function handle(e) {
	e.preventDefault();
	Promise.resolve(window.confirm("sure you want to delete it ?!!"))
	.then(confirm => {
		let id = this.firstElementChild.dataset.topicId
		return (confirm && Request.delete(`/api/topic/${id}`,{
			headers: [
				["X-Requested-With", "XMLHttpRequest"],
				["Content-Type", "application/json; charset=utf-8"]
			]
		})) || error("undo")
	})
	.then(response => {
		window.alert(response.message)
		return Request.get(window.location.pathname, {
			type: "document",
			headers: [
				["X-Requested-With", "XMLHttpRequest"]
			]
		});
	})
	.then(page => document.body = page.body )
	.catch(error => console.error(`error: ${error}`))
}

btns.forEach(btn => btn.addEventListener("click", handle.bind(btn)))