from flask import render_template, request, flash, redirect, url_for
from app import app, posts_store, members_store
from app import models, forms

app.secret_key = "private_key"

@app.route("/")
@app.route("/index")
def home():
	return render_template("index.html", posts=posts_store.get_all())

@app.route("/topic/add", methods=["GET", "POST"])
def add_topic():
	form = forms.TopicForm()
	if request.method == "POST":
		if form.validate_on_submit():
			new_post = models.Posts(request.form["title"], request.form["content"])
			posts_store.add(new_post)
			flash("new topic was created successfully!!")
			return redirect(url_for("home"))
		else:
			return render_template("add_topic.html", form=form)
	else:
		return render_template("add_topic.html", form=form)