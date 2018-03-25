from app import db
from datetime import datetime
import uuid

class Member(db.Model):

	__tablename__ = "members"
	
	id = db.Column(db.Integer, primary_key=True)
	user = db.Column(db.String(40), unique=True, nullable=False)
	name = db.Column(db.String(60), nullable=False)
	age = db.Column(db.Integer, nullable=False)
	p_id = db.Column(db.String(100), nullable=False)
	posts = db.relationship("Post", backref="members")

	def __init__(self, **kwargs):
		super(Member, self).__init__(**kwargs)
		self.p_id = str(uuid.uuid4())

	def __repr__(self):
		return "Name: {name},Age: {age}".format(**self.as_dict())
	
	def as_dict(self):
		return {
			"id": self.id,
			"user": self.user,
			"name": self.name,
			"age": self.age,
			"public_id": self.p_id,
			"posts": self.posts
		}

class MixinTimestamp(object):
	create_at = db.Column(db.DateTime, default=datetime.now())
	update_at = db.Column(db.DateTime, onupdate=datetime.now())

class Post(MixinTimestamp, db.Model):

	__tablename__ = "posts"

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(40), nullable=False)
	content = db.Column(db.String(800), nullable=False)
	member_id = db.Column(db.Integer, db.ForeignKey("members.id"), nullable=False)
	
	def __repr__(self):
		return "Title: {title}, Content: {content}".format(**self.as_dict())		
	
	def as_dict(self):
		return {
			"id": self.id,
			"title": self.title,
			"content": self.content,
			"member_id": self.member_id,
			"create_at": self.create_at and self.create_at.strftime("%Y-%m-%d %H:%M:%S"),
			"update_at": self.update_at and self.update_at.strftime("%Y-%m-%d %H:%M:%S")
		}