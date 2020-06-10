# Import the flask instance from our package
from app_pkg import flask_app
from flask import render_template


# Home route
@flask_app.route("/")
@flask_app.route("/index", methods=['GET', 'POST'])
def index():
    return render_template('hello.html')


# Blog route
@flask_app.route("/blog")
def blog():
    return "Hello Blog"
