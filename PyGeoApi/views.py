from app import app
from api import create_user, user_info
from tools import jsonify
from flask import request
from flask_jwt import jwt_required
# from flask import jsonify

@app.route("/hi")
def hello_world():
    return jsonify({"message": "hello there"})


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


@app.route("/token/<string:token>")
def user_detail_route(token):
    return jsonify({"user_info": user_info(token)})


@app.route('/protected')
@jwt_required()
def protected():
    return 'Success!'
