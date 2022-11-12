from flask import Flask
from flask_cors import CORS

from api.routes import rest_api

# Create App
app = Flask(__name__)

# load Config
app.config.from_object('api.config.BaseConfig')

# Connect Flask and FlaskRestX
rest_api.init_app(app)

# Enable CORS
CORS(app, resources={r"/api/*": {"origins": app.config["ALLOW_HOSTS"]}})
