"""
I keep app.py very thin.
"""
from flask import Flask

# mongodb
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()

db = client["geoapi"]
