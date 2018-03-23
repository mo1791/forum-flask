from flask_restful import Resource, Api, abort, reqparse
from app import app, posts_store
from app import models



api = Api(app, prefix="/api/v1")

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


class BaseTopic(Resource):
	def options(self):
		return {"allow": "GET, PUT, POST"},200, \
		{
			"Access-Control-Allow-Origin": "*",
			"Access-Control-Allow-Methods": "POST, PUT, GET",
			"Access-Control-Allow-Headers": "content-type, X-JWT-Token, X-Requested-With"
		}

@api.resource("/topic")
class TopicListApi(BaseTopic):
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

@api.resource("/topic/<int:id_>")
class TopicApi(BaseTopic):
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
