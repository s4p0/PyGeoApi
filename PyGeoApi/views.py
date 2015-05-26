from flask import request
# from flask import jsonify
from tools import jsonify


from app import app
from api import create_user, user_info


@app.route("/hi")
def hello_world():
    return jsonify({"message": "hello there"})


@app.route("/signup", methods=["POST"])
def signup_route():
    # pdb.set_trace()
    username = request.form["email"]
    password = request.form["password"]
    if username is not None and password is not None:
        return jsonify({"message": create_user(username, password)})
    return jsonify({"message": "something wrong with your credentials"})


@app.route("/token/<string:token>")
def user_detail_route(token):
    return jsonify({"user_info": user_info(token)})
