from flask import request, jsonify
from flask_restful import Resource, Api, abort, reqparse
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, jwt_optional
)
from app import app, posts_store
from app import models
from app import db
import datetime



api = Api(app, prefix="/api/v1")

app.config["SECRET_KEY"] = "private-key"
app.config["JWT_SECRET_KEY"] = "jwt-private-key"
app.config["JWT_HEADER_NAME"] = "X-JWT-Token"
app.config["JWT_HEADER_TYPE"] = "Forum"



parser = reqparse.RequestParser(trim=True, bundle_errors=True)


jwt = JWTManager(app)

@jwt.user_identity_loader
def add_identity(user):
	return str(user.id) + str(user.public_id)

@app.route("/auth", methods=["POST"])
def auth():
	if not request.is_json:
		return jsonify({"messg": "missing json request"}), 400
	parser.add_argument(
		"user", type=str, required=True, nullable=False
	)
	args = parser.parse_args(strict=True)
	username = args["user"]
	current_user = models.Member.query.filter_by(user=username).first()
	if not current_user:
		return jsonify({"messg": " user not found"}), 404
	token = create_access_token(identity=current_user)
	return jsonify({"access_token": token}), 201

@app.route("/dev-token", methods=["POST"])
def dev_token():
	id_ = int(get_jwt_identity()[0])
	current_user = models.Member.query.get(id_)
	expires = datetime.timedelta(days=365)
	token = create_access_token(identity=current_user, expires_delta=expires)
	return json({"log_access_token": token}), 201


@app.route("/create", methods=["POST"])
def new_user():
	if not request.is_json:
		return jsonify({"messg": "missing json request"}), 400
	parser.add_argument(
		"user", type=str, required=True, nullable=False
	)
	parser.add_argument(
		"name", type=str, required=True, nullable=False
	)
	parser.add_argument(
		"age", type=int, required=True, nullable=False
	)
	args = parser.parse_args(strict=True)
	new_user = models.Member(user=args["user"], name=args["name"], age=args["age"])
	db.session.add(new_user)
	db.session.commit()
	return jsonify({
		"messg": "new user has been created", 
		"user": new_user.as_dict()
	}), 200


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
	
	@jwt_optional
	def get(self):
		posts = [post.as_dict() for post in posts_store.get_all()]
		return posts, {"Access-Control-Allow-Origin": "*"}
	
	@jwt_required
	def post(self):
		current_id = int(get_jwt_identity()[0])
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
	
	@jwt_optional
	def get(self, id_):
		post = posts_store.get_by_id(id_)
		try:
			result = post.as_dict()
		except AttributeError:
			result = abort(404, message="topic %d doesn't exist" % id_)
		return result
	
	@jwt_required
	def put(self, id_):
		post = posts_store.get_by_id(id_)
		parser.add_argument(
			"title", type=str, required=True, nullable=False
		)
		parser.add_argument(
			"content", type=str, required=True, nullable=False
		)
		args = parser.parse_args(strict=True)
		try:
			post.title = args["title"]
			post.content = args["content"]
			posts_store.update(post)
			result = {
				"message":"topic updated successfully?!!",
				"updated": post.as_dict()
			}
		except AttributeError:
			result = abort(404, message="topic %d doesn't exist" % id_)
		return result
	
	@jwt_required
	def delete(self, id_):
		if not posts_store.entity_exist(id_):
			abort(404, message="topic %d doesn't exist" % id_)
		posts_store.delete(id_)
		return {"message": "Sadly!! topic was deleted"} 
