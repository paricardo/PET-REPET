from flask import Flask
from src.routes.users_route import users

def create_app():
    app = Flask(__name__)

    app.register_blueprint(users)


    return app