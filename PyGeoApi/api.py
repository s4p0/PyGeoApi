"""
basics api methods
"""
from uuid import uuid4
from app import db

# main functions
def create_user(username, password):
    if no_user(username):
        return add_new_user(username, password)
    return "This username exists"

def find_user(username, password):
    return db["users"].find_one({"username": username, "password": password}, {"password": False})

def user_info(token):
    return db["users"].find_one({"token": token}, {"password": False})


# helper functions
def no_user(username):
    return db["users"].find_one({"username": username}) == None


def add_new_user(username, password):
    user = {"username": username, "password": password, "token": str(uuid4())}
    db["users"].insert_one(user)
    if user is None:
        return "something went wrong / adding user"
    return "successfully added!"


