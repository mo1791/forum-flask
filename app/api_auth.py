from flask import request, jsonify
from flask_jwt_extended import (
	JWTManager, create_access_token, 
	get_jwt_identity, jwt_required, jwt_optional
)
from app import app, models, db
from api import parser
import datetime


jwt = JWTManager(app)


@jwt.user_identity_loader
def add_identity(user):
	return str(user.id) + str(user.p_id)



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
@jwt_required
def dev_token():
	current = get_jwt_identity()
	id_ = int(current[0])
	current_user = models.Member.query.get(id_)
	expires = datetime.timedelta(days=365)
	token = create_access_token(identity=current_user, expires_delta=expires)
	return jsonify({"long_access_token": token}), 201


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
