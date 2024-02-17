from flask import Flask
from flask_cors import CORS
from .shop import shop
from .auth import auth

from .config import Config

def create_app():
    
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    app.register_blueprint(shop)
    app.register_blueprint(auth)
    
    return app