from flask import Blueprint, request, jsonify
from src.services.auth_service import AuthService

auth = Blueprint("auth", __name__)
service = AuthService()


@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "error": "email e password são obrigatórios"
        }), 400

    result, status_code = service.login(email, password)

    return jsonify(result), status_code


@auth.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({
            "error": "name, email e password são obrigatórios"
        }), 400

    result, status_code = service.register(name, email, password)

    return jsonify(result), status_code