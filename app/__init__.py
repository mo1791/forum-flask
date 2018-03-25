from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

__dirname = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app import dummy_data, stores

members_store = stores.MemberStores()
posts_store = stores.PostStores()

#dummy_data.store(members_store, posts_store)

from app import views, api