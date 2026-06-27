from flask import Flask
from flask_jwt_extended import JWTManager

from config import DevelopmentConfig
from src.routes.users.users_route import users
from src.routes.users.users_ui_route import users_ui
from src.routes.auths.auth_route import auth
from src.routes.customers.customers_route import customers
from src.routes.pets.pets_route import pets
from src.routes.appointments.appointments_route import appointment
from src.routes.customers_plan.customers_plan_route import customer_plan
from src.routes.plan.plans_route import plan
from src.routes.service.services_route import service_route

jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)

    jwt.init_app(app)

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(users, url_prefix='/api/users')
    app.register_blueprint(users_ui, url_prefix='/api/users')
    app.register_blueprint(appointment, url_prefix='/api/appointment')
    app.register_blueprint(customers, url_prefix='/api/customers')
    app.register_blueprint(customer_plan, url_prefix='/api/customer_plan')
    app.register_blueprint(pets, url_prefix='/api/pet')
    app.register_blueprint(plan, url_prefix='/api/plan')
    app.register_blueprint(service_route, url_prefix='/api/service')

    return app