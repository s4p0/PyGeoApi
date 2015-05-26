"""
I keep app.py very thin.
"""
from flask import Flask
# JWT
# from flask_jwt import JWT
# mongodb
from pymongo import MongoClient

app = Flask(__name__)
# jwt = JWT(app)

client = MongoClient()
db = client["geoapi"]
