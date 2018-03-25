const Home = Vue.extend({
	template: "<router-view></router-view>"
})
const Index = Vue.extend({
	data() {
		return {
			loading: false,
			posts: null,
			error: null
		}
	},
	methods: {
		fetchPosts() {
			this.error = this.posts = null
			this.loading = true
			this.$http.get(`/api/v1/topic`, {headers: {"X-JWT-Token": `Forum ${token}`}})
			.then(response => {
				this.loading = false
				this.posts = response.body
			}, error => {
				console.log(`error :${error}`)
			})
		}
	},
	created() {
		this.fetchPosts()
	},
	template: `
		<div class="index">
			<div v-if="loading" class="loading">
				loading data ....
			</div>
			<div v-if="posts" class="table">
				<table>
					<tr>
						<th>Topic</th>
						<th>Edit</th>
						<th>Delete</th>
						<th>Show</th>
					</tr>
					<tr v-for="post in posts">
						<td>
							{{ post.title }}
						</td>
						<td>
							<router-link :to="{name: 'edit', params: {id: post.id }}" class="btn btn-warning btn-sm">Edit</router-link>
						</td>
						<td>
							<router-link :to="{name: 'delete', params: {id: post.id }}" class="btn btn-danger btn-sm">Delete</router-link>
						</td>
						<td>
							<router-link :to="{name: 'show', params: {id: post.id }}" class="btn btn-primary btn-sm">Show</router-link>
						</td>
					</tr>
				</table>
			</div>
			<div v-if="error" class="error">
				Error ....
			</div>
		</div>
	`
})

const NotFound = {
	template: `
		<div class="notfound">
			this page not found
		</div>
	`
}
const router = new VueRouter({
	routes: [
		{name: "notfound", path: "*", component: NotFound, meta: {title: "Not Found"}},
		{
			name: "home",
			path: "/",
			component: Home,
			children: [
				{
					name: "index",
					path: "",
					component: Index,
					meta: {title: "Forum | Home"},
				},
				{
					name: "add",
					path: "/add",
					component: Add,
					meta: {title: "Forum | Add"}
				},
				{
					name: "edit",
					path: "/edit/:id",
					component: Edit,
					meta: {title: "Forum | Edit"}
				},
				{
					name: "show",
					path: "/topic/:id",
					component: Show,
					meta: {title: "Forum | Show"}
				},
				{
					name: "delete",
					path: "/delete/:id",
					component: Delete,
					meta: {title: "Forum | Delete"}
				}
			]
		}
	]
})

router.beforeEach((to, from, next) => {
	document.title = to.meta.title
	next()
})



const app = new Vue({
	router,
	template: "<router-view></router-view>"
}).$mount("#app")