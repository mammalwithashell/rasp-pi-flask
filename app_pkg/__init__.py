# Import the flask library
from flask import Flask

# Name my flask instance "flask_app"
flask_app = Flask(__name__)
flask_app.debug = True

# Import routes into the package
from app_pkg import routes
