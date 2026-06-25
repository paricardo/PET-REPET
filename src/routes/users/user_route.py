from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.services.users_service import UserService

users = Blueprint('users', __name__, url_prefix="/users")
service = UserService()


@users.route('/', methods=['GET'])
@jwt_required()
def list_all_users():
    result = service.get()
    return jsonify(result), 200


@users.route('/<string:id_user>', methods=['GET'])
@jwt_required()
def list_user(id_user):
    result = service.getById(id_user)

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]

    return jsonify(result), 200


@users.route('/', methods=['POST'])
@jwt_required()
def add_user():
    data = request.get_json()

    current_user_id = get_jwt_identity()
    current_user = service.get_user_entity(current_user_id)

    result = service.add(data, current_user=current_user)
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    return jsonify(result), 201


@users.route('/<string:id_user>', methods=['PUT'])
@jwt_required()
def update_user(id_user):
    data = request.get_json()

    result = service.update(id_user, **data)

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]

    return jsonify(result), 200


@users.route('/<string:id_user>', methods=['DELETE'])
@jwt_required()
def delete_user(id_user):
    
    result = service.delete(id_user)

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]

    return jsonify(result), 200