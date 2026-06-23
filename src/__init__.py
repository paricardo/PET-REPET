from flask import Flask
from flask_jwt_extended import JWTManager

from config import DevelopmentConfig
from src.routes.users.user_route import users
from src.routes.users.user_ui_route import users_ui
from src.routes.auths.auth_route import auth

jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)

    jwt.init_app(app)

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(users, url_prefix='/api/users')
    app.register_blueprint(users_ui, url_prefix='/users')

    return app