from flask import (
    Blueprint, 
    render_template,
    request,
    redirect,
    url_for
)
from src.database.in_memory.db_in_memory import USERS
from src.service.format_data import is_valid_email


users_bp = Blueprint('users', __name__)


"""
    ROTAS DE USUÁRIOS 
    (GET, POST) form_users > renderiza o formulario de cadastro
    (GET) list_all_users > renderiza uma lista de usuarios
    (GET) info_users
"""

# TELAS DE USUÁRIOS
@users_bp.route('/', methods=['GET'])
def list_all_users():

    return render_template("users.html", USERS=USERS)



@users_bp.route('/user')
def list_one_user():
    
    search = request.args.get("search", "").strip()

    search_lower = search.lower()

    users_found = [
        user
        for user in USERS
        if (
            search_lower in user["name"].lower()
            or search_lower in user["email"].lower()
        )
    ]

    return render_template(
        "users.html",
        USERS=users_found
    )



@users_bp.route('/info/<int:id_user>', methods=['GET'])
def info_users(id_user):

    user = next(
        (u for u in USERS if u['id'] == id_user),
        None
    )

    if not user:
        return "Usuário não encontrado", 404

    return render_template(
        "info_users.html",
        user=user
    )
    

@users_bp.route('/add', methods=['GET'])
def form_users():

    return render_template("add_users.html")


@users_bp.route('/edit/<int:id_user>', methods=['GET'])
def form_edit_users(id_user):
    
    user = next((u for u in USERS if u['id'] == id_user), None)

    if not user:
        return "Usuário não encontrado", 404

    return render_template("form_edit_users.html", user=user, edit=True)




"""
    ROTAS DO CRUD DE USUÁRIOS
"""

@users_bp.route('/create', methods=['POST'])
def create_users():

    new_user = request.form.to_dict()

    if not new_user:
        return "Dados inconsistentes para cadastro", 400
    
    if new_user['is_active'] == "true":
        is_active = True
    else:
        is_active = False

    email = is_valid_email(new_user['email'])

    if not email == False:
        return "Email inválido", 400

    data = {
        "id": len(USERS) + 1,
        "name": new_user['name'],
        "email": email,
        "password_hash": new_user['password'],
        "role": new_user['role'],
        "is_active": is_active
    }

    USERS.append(data)

    return redirect(url_for('users.list_all_users'))


@users_bp.route('/update/<int:id_user>', methods=['POST'])
def update_users(id_user):

    user = next((u for u in USERS if u['id'] == id_user), None)

    if not user:
        return "Usuário não encontrado", 404

    form = request.form.to_dict()

    user['name'] = form.get('name')
    user['email'] = form.get('email')
    user['password_hash'] = form.get('password')
    user['role'] = form.get('role')
    user['is_active'] = form.get('is_active') == "true"

    return redirect(
        url_for(
            'users.info_users',
            id_user=id_user
        )
    )


@users_bp.route('/del/<int:id_user>', methods=['POST'])
def delete_users(id_user):

    user = next((u for u in USERS if u['id'] == id_user), None)

    if not user:
        return "Usuario não encontrado", 404
    
    USERS.remove(user)

    return redirect(url_for('users.list_all_users'))