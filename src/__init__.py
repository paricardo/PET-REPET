from flask import Flask
#from flask_jwt_extended import JWTManager

from config import DevelopmentConfig
from src.routes.users_route import users_bp
from src.routes.customers_route import customers_bp

#jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)

   # jwt.init_app(app)

    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(customers_bp, url_prefix="/customers")


    return app