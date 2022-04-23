from flask import Flask
from config.config import config_by_name

# Creating app
app = Flask(__name__)

# load configuration
config = config_by_name['local']

# Initializing blueprints
from api_auth.controller import auth

app.register_blueprint(auth)

if __name__ == '__main__':
	app.run()
