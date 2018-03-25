const Add = Vue.extend({
	mixins: [mixin],
	methods: {
		post_handler(e) {
			const data = this.getData()
			this.$http.post(`/api/v1/topic`, data, {headers: {"X-JWT-Token": `Forum ${token}`}})
			.then(response => {
				response.ok && window.alert(response.body.message)
				this.$router.push({name: "index"})
			}, error => {
				console.log(`error: ${error}`)
			})
		}
	},
	template: `
		<div class="add">
			<form @submit.prevent="post_handler" method="post" id="form">
				<div class="form-group">
					<label for="title">Title :</label>
					<input type="text" name="title" class="form-control" id="title">
				</div>
				<div class="form-group">
					<label for="content">Content :</label>
					<textarea name="content" class="form-control" rows="6" id="content"></textarea>
				</div>
				<div class="form-group">
					<button type="submit" class="btn btn-primary">Create Topic</button>
				</div>
			</form>
		</div>
	`
})