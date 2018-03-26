from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://pcswhxjwpdfali:e4371b669a020fd188ceec2d1b8382e37167308a09c0fcb36fb6bdfb9451c355@ec2-54-243-28-109.compute-1.amazonaws.com:5432/db807aat9jelok"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from app import dummy_data, stores

members_store = stores.MemberStores()
posts_store = stores.PostStores()

#dummy_data.store(members_store, posts_store)

from app import views, api