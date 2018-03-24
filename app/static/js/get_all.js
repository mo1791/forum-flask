const Home = {
	template: "<router-view></router-view>"
}

const Index = {
	data: {
	  message: this.getFromForm()
	}
	template: `
		<div class="index">
			hello from index page {{ message }}
		</div>
	`
}