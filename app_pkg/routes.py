from app_pkg import flask_app

@app.route("/")
@app.route("/index")
def hello():
	return "Hello World!"

