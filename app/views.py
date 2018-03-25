from flask import render_template
from app import app, posts_store, members_store
from app import models


@app.route("/")
@app.route("/index")
def home():
	return render_template("index.html")

@app.errorhandler(404)
def not_found(err):
	return render_template("errors/404.html"), 404