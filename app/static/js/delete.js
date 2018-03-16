const btns = document.querySelectorAll(".delete")
const error = err => { throw Error(err) }


function handle(e) {
	e.preventDefault();
	Promise.resolve(window.confirm("sure you want to delete it ?!!"))
	.then(confirm => {
		let id = this.dataset.topicId
		return (confirm && Request.delete(`/api/topic/${id}`,{
			headers: [
				["X-Requested-With", "XMLHttpRequest"],
				["Content-Type", "application/json; charset=utf-8"]
			]
		})) || error("undo")
	})
	.then(response => {
		window.alert(response.message)
		window.location = window.location.href
	})
	.catch(error => {
		console.error(`error: ${error}`)
	})
}

btns.forEach(btn => btn.addEventListener("click", handle.bind(btn)))