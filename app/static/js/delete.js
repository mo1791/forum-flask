const Delete = Vue.extend({
	methods: {
		delete_handler(e) {
			this.$http.delete(`/api/v1/topic/${this.$route.params.id}`, {headers: {"X-JWT-Token": `Forum ${token}`}})
			.then(response => {
				response.ok && window.alert(response.body.message)
				this.$router.push({name: "index"})
			}, error => {
				console.log(`error: ${error}`)
			})
		},
		cancel_handler(e) {
			this.$router.push({name: "index"})
		}
	},
	template: `
		<div class="delete" style="margin-top:100px">
			<div class="row">
				<div class="col-sm-3"></div>
				<div class="col-sm-6">
					<div class="card text-white bg-danger mb-3" style="max-width: 20rem;">
					  <div class="card-header">Confirmation</div>
					  <div class="card-body">
					    <h4 class="card-title">Sure you want to delete this topic!!</h4>
					    <button @click="delete_handler" type="button" class="btn btn-default btn-sm">Delete</button>	
					    <button @click="cancel_handler" type="button" class="btn btn-default btn-sm">Cancel</button>	
					  </div>
					</div>
				</div>
				<div class="col-sm-3"></div>
			</div>
		</div>
	`
})