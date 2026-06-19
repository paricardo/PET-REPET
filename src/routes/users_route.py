from flask import Blueprint, render_template, request, jsonify
from src.services.users_service import UserService


users = Blueprint('users', __name__, url_prefix="/users")

service = UserService()

"""
    ROTAS DE USERS

    ROTAS DE TEMPLATES
        - (GET) /users/ -> renderiza a tela de usuarios
        - (GET, POST) /users/ -> renderiza a tela de cadastro de usuarios
        - (GET) -> renderiza a tela de informações de usuarios 

    ROTAS DE CRUD
        - (GET)    /users/ -> listar todos os usuarios
        - (GET)    /users/<int:id_user> -> obter um usuario
        - (POST)   /users/ -> cria um usuario no banco
        - (PUT)    /users/<int:id_user> -> edita o usuario no banco
        - (DELETE) /users/<int:id_user> -> deleta um usuario do banco 

"""

# ROTAS DE TEMPLATES DE USUÁRIOS

@users.route('/list-users', methods=['GET'])
def list_users():
    # renderiza tela de usuarios
    return render_template("users.html")

@users.route('/add-users', methods=['GET', 'POST'])
def form_users():
    # renderiza tela de cadastro de usuarios
    return render_template("add_users.html")

@users.route('/info-users', methods=['GET'])
def info_users():
    # renderiza tela de informações de clientes
    return render_template("info_users.html")


# ROTAS DE CRUD DE USUÁRIOS

@users.route('/', methods=['GET'])
def get():
    # listar todos do usuarios
    pass

@users.route('/<int:id_user>', methods=['GET'])
def getById(id_user):
    # lista um usuario por id
    pass

@users.route('/', methods=['POST'])
def add():
    # cria um usuario no banco
    data = request.get_json()

    result = service.add(data)

    return jsonify(result), 201

@users.route('/<int:id_user>', methods=['PUT'])
def update(id_user):
    # edita um usuario por id
    pass

@users.route('/<int:id_user>', methods=['DELETE'])
def delete(id_user):
    # deleta um usuario por id
    pass