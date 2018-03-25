const Edit = Vue.extend({
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
			this.error = this.post = null
			this.loading = true
			this.$http.get(`/api/v1/topic/${this.$route.params.id}`, {headers: {"X-JWT-Token": `Forum ${token}`}})
			.then(response => {
				this.loading = false
				this.post = response.body
			}, error => {
				this.loading = false
				this.error = true
				console.log(`error: ${error}`)
			})
		},
		update_handler(e) {
			const data = this.getData()
			this.$http.put(`/api/v1/topic/${this.$route.params.id}`, data, {headers: {"X-JWT-Token": `Forum ${token}`}})
			.then(response => {
				console.log(response.body)
				response.ok && window.alert(response.body.message)
				this.$router.push({name: "index"})
			}, error => {
				this.error = true
				console.log(`error: ${error}`)
			})
		}
	},
	created() {
		this.fetchPost()
	},
    template: `
        <div class="edit">
        	<div v-if="loading" class="loading">
        		Loading Data.....
        	</div>
            <div v-if="post" class="form">
				<form @submit.prevent="update_handler" method="post" id="form">
					<div class="form-group">
						<label for="title">Title :</label>
						<input type="text" name="title" class="form-control" id="title" :value="post.title">
					</div>
					<div class="form-group">
						<label for="content">Content :</label>
						<textarea name="content" class="form-control" rows="6" id="content">{{ post.content }}</textarea>
					</div>
					<div class="form-group">
						<button type="submit" class="btn btn-primary">Create Topic</button>
					</div>
				</form>
			</div>
			<div v-if="error" class="error">
				Error....
			</div>
        </div>
    `
})