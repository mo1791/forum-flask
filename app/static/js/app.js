const Home = {
	template: "<router-view></router-view>"
}

const Index = {
	template: `
		<div class="index">
			hello from index page
		</div>
	`
}

const Add = {
	template: `
		<div class="add">
			hello from add page
		</div>
	`
}

const Edit = {
	template: `
		<div class="edit">
			hello from edit page
		</div>
	`
}

const Show = {
	template: `
		<div class="show">
			hello from show page
		</div>
	`
}

const Delete = {
	template: `
		<div class="delete">
			hello from delete page
		</div>
	`
}





Vue.use(Router)

const router = new Router({
	mode: "history",
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

router.beforEach((from, to, next) => {
	document.title = to.meta.title
	next()
})

new Vue({
	router,
	template: "<router-view></router-view>"
}).$mount("#app")