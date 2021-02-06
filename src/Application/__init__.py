from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from src.Application import Routes

app: Flask = Flask(__name__)

application = Api(app)
CORS(app)
Routes.add_routes(application)
