"""
basics api methods
"""
from uuid import uuid4
from app import db

# main functions


def create_user(email, password):
    if no_user(email):
        return add_new_user(email, password)
    return "This email exists"


def user_info(token):
    return db["users"].find_one({"token": token},{"password": False})

# helper functions


def no_user(email):
    return db["users"].find_one({"email": email}) == None


def add_new_user(email, password):
    user = {"email": email, "password": password, "token": str(uuid4())}
    db["users"].insert_one(user)
    if user is None:
        return "something went wrong / adding user"
    return "successfully added!"
