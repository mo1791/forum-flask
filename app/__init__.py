from flask import Flask
from app import dummy_data, stores

app = Flask(__name__)

members_store = stores.MemberStores()
posts_store = stores.PostStores()

dummy_data.store(members_store, posts_store)

from app import views