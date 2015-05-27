"""
main executable file
"""
from app import app
from auth import *
from api import *
from views import *
from flask_cors import CORS
c = CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
