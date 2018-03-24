const mixin = {
	methods: {
		getData: function() {
			const form = document.querySelector("#form")
			const data = new FormData(form)
			const vals = Array.from(data.entities()).reduce((obj, [name, value]) => {
				obj[name] = value
				return obj
			}, {})
			return JSON.stringify(vals)
		}
	},
}

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
			this.$http.get(`/api/v1/topic`).then(response => {
				this.loading = false
				console.log(response.body)
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
			hello world
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