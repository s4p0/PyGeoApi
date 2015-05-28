from app import app, db
from api import find_user, user_info
from flask_jwt import JWT, current_app


app.config['JWT_SECRET_KEY'] = "ahsdkjahduiahydiuahdiuashdl23137808asdajdoasudo==--*/*1"
app.config['JWT_AUTH_URL_RULE'] = '/authenticate'
jwt = JWT(app)


@jwt.authentication_handler
def authenticate(username, password):
    user = find_user(username, password)
    return user


@jwt.user_handler
def load_user(payload):
    return user_info(payload["user_token"])


@jwt.payload_handler
def make_payload(user):
    return {'user_token': user["token"]}
