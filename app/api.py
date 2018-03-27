from flask_restful import Resource, Api, abort, reqparse
from app import app, posts_store, models, db


api = Api(app, prefix="/api/v1")

app.config["SECRET_KEY"] = "private-key"
app.config["JWT_SECRET_KEY"] = "jwt-private-key"
app.config["JWT_HEADER_NAME"] = "X-JWT-Token"
app.config["JWT_HEADER_TYPE"] = "Forum"



parser = reqparse.RequestParser(trim=True, bundle_errors=True)

import api_auth


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
	
	@api_auth.jwt_optional
	def get(self):
		posts = [post.as_dict() for post in posts_store.get_all()]
		return posts, {"Access-Control-Allow-Origin": "*"}
	
	@api_auth.jwt_required
	def post(self):
		current_id = int(api_auth.get_jwt_identity()[0])
		parser.add_argument(
			"title", type=str, required=True, nullable=False
		)
		parser.add_argument(
			"content", type=str, required=True, nullable=False
		)
		args = parser.parse_args(strict=True)
		post = models.Post(title=args["title"], content=args["content"], member_id=current_id)
		posts_store.add(post)
		return {
			"message": "new topic was created successfully?!!",
			"posted": post.as_dict()
		}


@api.resource("/topic/<int:id_>")
class TopicApi(BaseTopic):
	
	@api_auth.jwt_optional
	def get(self, id_):
		post = posts_store.get_by_id(id_)
		try:
			result = post.as_dict()
		except AttributeError:
			result = abort(404, message="topic %d doesn't exist" % id_)
		return result
	
	@api_auth.jwt_required
	def put(self, id_):
		post = posts_store.get_by_id(id_)
		parser.add_argument(
			"title", type=str, required=True, nullable=False
		)
		parser.add_argument(
			"content", type=str, required=True, nullable=False
		)
		args = parser.parse_args(strict=True)
		title = args["title"]
		content = args["content"]
		if len(content) > 790:
			return { "messg": "content exceed max len" }, 400
		if len(title) > 35:
			return { "message", "title exceed max len" }, 400
		try:
			post.title = title
			post.content = content
			posts_store.update(post)
			result = {
				"message":"topic updated successfully?!!",
				"updated": post.as_dict()
			}
		except AttributeError:
			result = abort(404, message="topic %d doesn't exist" % id_)
		return result
	
	@api_auth.jwt_required
	def delete(self, id_):
		if not posts_store.entity_exist(id_):
			abort(404, message="topic %d doesn't exist" % id_)
		posts_store.delete(id_)
		return {"message": "Sadly!! topic was deleted"} 
