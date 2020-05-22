# Main application that is being run
from app_pkg import *

if __name__ == "__main__":
	flask_app.run(host='0.0.0.0', port=8080)
