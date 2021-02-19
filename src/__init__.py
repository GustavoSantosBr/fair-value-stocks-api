from flask import Flask
from flask_cors import CORS

from src.Application import Routes, blueprint_stocks


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(blueprint_stocks)
    CORS(app)
    return app
