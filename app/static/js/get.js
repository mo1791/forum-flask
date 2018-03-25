const Show = Vue.extend({
	mixins: [mixin],
	data() {
		return {
			loading: false,
			post: null,
			error: null
		}
	},
	methods: {
		fetchPost() {
			this.post = this.error = null
			this.loading = true
			this.$http.get(`/api/v1/topic/${this.$route.params.id}`, {headers: {"X-JWT-Token": token}})
			.then(response => {
				this.loading = false
				this.post = response.body
			}, error => {
				this.loading = false
				this.error = true
				console.log(`error: ${error}`)
			})
		}
	},
	created() {
		this.fetchPost()
	},
	template: `
		<div class="show">
			<div v-if="loading" class="loading">
				loading data.....
			</div>
			<div v-if="post" class="post">
				<div class="row" style="margin-top: 100px;">
					<div class="col-md-2"></div>
					<div class="col-md-8">
						<div class="card border-primary">
						 <div class="card-body">
						    <h2 class="card-title">{{ post.title }}</h2>
						    <p class="card-text" style="font-size: 13px;">{{ post.content }}</p>
						    <h6 class="card-subtitle mb-2 text-muted" style="font-size: 10px;">Created at:{{ post.create_at }}</h6>
						  </div>
						</div>
					</div>
					<div class="col-md-2"></div>
				</div>
			</div>
			<div v-if="error" class="error">
				Error....
			</div>
		</div>
	`
})