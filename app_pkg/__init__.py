# Import the flask library
from flask import Flask

# Name my flask instance "flask_app"
flask_app = Flask(__name__)

# Import routes into the package
from app_pkg import routes
