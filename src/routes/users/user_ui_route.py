from flask import Blueprint, render_template
from flask_jwt_extended import jwt_required

users_ui = Blueprint('users_ui', __name__, url_prefix="/users")

"""
ROTAS DE TEMPLATES DE USUÁRIOS (PROTEGIDAS COM JWT)

- (GET) /users/list-users  -> tela de listagem
- (GET, POST) /users/add-users -> tela de cadastro
- (GET) /users/info-users -> tela de detalhes
"""

# LISTAGEM DE USUÁRIOS
@users_ui.route('/list-users', methods=['GET'])
@jwt_required()
def list_users():
    return render_template("users.html")


# FORMULÁRIO DE USUÁRIO
@users_ui.route('/add-users', methods=['GET', 'POST'])
@jwt_required()
def form_users():
    return render_template("add_users.html")


# INFORMAÇÕES DO USUÁRIO
@users_ui.route('/info-users', methods=['GET'])
@jwt_required()
def info_users():
    return render_template("info_users.html")