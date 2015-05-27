from app import app
from api import create_user, user_info, add_or_replace_layers, select_layers
from tools import jsonify
from flask import request
from flask_jwt import jwt_required, current_user


# public routes
@app.route("/signup", methods=["POST"])
def signup_route():
    if request.form:
        username = request.form["username"]
        password = request.form["password"]
    if request.json:
        username = request.json["username"]
        password = request.json["password"]
    if username is not None and password is not None:
        return jsonify({"message": create_user(username, password)})
    return jsonify({"message": "something wrong with your credentials"})


# only protected routes
@app.route('/me')
@jwt_required()
def me_route():
    current_user.pop("token")
    return jsonify(current_user)


@app.route('/me/features', methods=["GET", "POST"])
@jwt_required()
def layers_route():
    # current_user
    if request.method == "GET":
        return jsonify(select_layers(current_user))
    if request.method == "POST":
        return jsonify(add_or_replace_layers(current_user, request.json))
    pass
