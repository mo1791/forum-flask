from flask import render_template, request, flash, redirect, url_for, abort
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
	if request.method == "POST" and form.validate_on_submit():
		new_post = models.Posts(request.form["title"], request.form["content"])
		posts_store.add(new_post)
		flash("new topic was created successfully!!")
		return redirect(url_for("home"))
	else:
		return render_template("add_topic.html", form=form)

@app.route("/topic/show/<int:id_>")
def show_topic(id_):
	post = posts_store.get_by_id(id_)
	if post is None:
		abort(404)
	return render_template("show_topic.html", post=post)

@app.route("/topic/edit/<int:id_>", methods=["GET", "POST"])
def edit_topic(id_):
	post = posts_store.get_by_id(id_)
	form = forms.TopicForm()
	if post is None:
		abort(404)
	if request.method == "POST" and form.validate_on_submit():
		post.title = request.form["title"]
		post.content = request.form["content"]
		posts_store.update(post)
		flash("topic was updated successfully", "success")
		return redirect(url_for("home"))
	else:
		form.content.data = post.content
		return render_template("edit_topic.html", form=form, post=post)

@app.route("/topic/delete/<int:id_>")
def delete_topic(id_):
	if posts_store.entity_exist(id_):
		posts_store.delete(id_)
		flash("Sadly!! deletion does occur successfully", "success")
		return redirect(url_for("home"))
	else:
		abort(404)

@app.route("/posts")
def all_posts():
	posts = posts_store.get_all()
	return render_template("show_all.html", posts=posts)

@app.errorhandler(404)
def not_found(err):
	return render_template("errors/404.html"), 404

@app.errorhandler(405)
def not_allowed(err):
	return "The request method is not allowed!!", 405