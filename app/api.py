from flask_restful import Resource, Api, abort, reqparse
from app import app, posts_store
from app import models



api = Api(app)

parser = reqparse.RequestParser(trim=True, bundle_errors=True)
parser.add_argument(
	"title",
	type=str,
	required=True,
	nullable=False
)
parser.add_argument(
	"content",
	type=str,
	required=True,
	nullable=False
)
parser.add_argument(
	"csrf_token",
	type=str,
	required=True,
	nullable=False
)

@api.resource("/api/topic")
class TopicListApi(Resource):
	def get(self):
		posts = [post.__dict__() for post in posts_store.get_all()]
		return posts
	def post(self):
		args = parser.parse_args(strict=True)
		post = models.Posts(args["title"], args["content"])
		posts_store.add(post)
		return {
			"message": "new topic was created successfully?!!",
			"posted": post.__dict__()
		}

@api.resource("/api/topic/<int:id_>")
class TopicApi(Resource):
	def get(self, id_):
		post = posts_store.get_by_id(id_)
		try:
			result = post.__dict__()
		except AttributeError:
			result = abort(404, message="topic %d doesn't exist" % id_)
		return result
	def put(self, id_):
		post = posts_store.get_by_id(id_)
		args = parser.parse_args(strict=True)
		try:
			post.title = args["title"]
			post.content = args["content"]
			posts_store.update(post)
			result = {
				"message":"topic updated successfully?!!",
				"updated": post.__dict__()
			}
		except AttributeError:
			result = abort(404, message="topic %d doesn't exist" % id_)
		return result
	def delete(self, id_):
		if not posts_store.entity_exist(id_):
			abort(404, message="topic %d doesn't exist" % id_)
		posts_store.delete(id_)
		return {"message": "Sadly!! topic was deleted"} 
