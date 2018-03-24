const router = new VueRouter({
	routes: [
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

new Vue({
	router,
	methods: {
		getFromForm()  {
			return "hello world"
		}
	}
	template: "<router-view></router-view>"
}).$mount("#app")