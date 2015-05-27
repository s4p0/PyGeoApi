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
    return db["users"].find_one(
        {"username": username, "password": password},
        {"password": False})


def user_info(token):
    return db["users"].find_one({"token": token})


# helper functions
def no_user(username):
    return db["users"].find_one({"username": username}) == None


def add_new_user(username, password):
    user = {"username": username, "password": password, "token": str(uuid4())}
    db["users"].insert_one(user)
    if user is None:
        return "something went wrong / adding user"
    return "successfully added!"


def add_or_replace_layers(user, new_layer):
    updated = db["users"].update_one(
        {"token": user["token"]},
        {"$addToSet": {"layers": new_layer}})
    return updated.raw_result


def select_layers(user):
    layers = db["users"].find_one({"token": user["token"]}, {"layers": True})
    return layers
