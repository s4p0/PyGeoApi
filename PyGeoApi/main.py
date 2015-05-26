"""
main executable file
"""
from app import app
from api import *
from views import *
from auth import *

if __name__ == '__main__':
    app.run(debug=True)
