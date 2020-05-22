from app_pkg import flask_app

@flask_app.route("/")
@flask_app.route("/index")
def hello():
	return "Hello World!"

