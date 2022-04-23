from flask import Flask
from config.config import config_by_name

# Creating app
app = Flask(__name__)

# load configuration
config = config_by_name['local']

# Initializing blueprints
from api.api_auth import api_auth
from api.api_upload import api_upload
from api.api import api

app.register_blueprint(api)
app.register_blueprint(api_auth)
app.register_blueprint(api_upload)

if __name__ == '__main__':
	app.run()
