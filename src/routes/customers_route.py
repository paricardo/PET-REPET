from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for
)
from src.database.in_memory.db_in_memory import CUSTOMERS
from src.service.format_data import *
customers_bp = Blueprint('customers', __name__)

"""
Tutores/donos dos pets.

| Campo        | Tipo      | Observação     |
| ------------ | --------- | -------------- |
| `id`         | UUID / PK |                |
| `name`       | string    |                |
| `phone`      | string    |                |
| `email`      | string    | opcional       |
| `notes`      | text      | opcional       |
| `is_active`  | boolean   | default `true` |
| `created_at` | datetime  |                |

| `pets`       | string    |                |

"""

"""
  ABAIXO TEMOS AS TELAS DE CLIENTES
"""

@customers_bp.route('/', methods=['GET'])
def list_all_customers():

    return render_template("clients.html", CUSTOMERS=CUSTOMERS)

@customers_bp.route("/customer")
def list_one_customer():

    search = request.args.get("search", "").strip()

    search_lower = search.lower()

    search_phone = format_phone(search)
    search_cpf = format_cpf(search)

    customers_found = [
        customer
        for customer in CUSTOMERS
        if (
            search_lower in customer["name"].lower()
            or customer["phone"] == search_phone
            or customer["cpf"] == search_cpf
        )
    ]

    return render_template(
        "clients.html",
        CUSTOMERS=customers_found
    )


@customers_bp.route('/info/<int:id_customer>', methods=['GET'])
def info_customers(id_customer):
    
    customer = next(
        (u for u in CUSTOMERS if u['id'] == id_customer),
        None
    )

    if not customer:
        return "Cliente não econtrado", 404
    
    return render_template(
        "info_clients.html",
        customer=customer
    )

@customers_bp.route('/add', methods=['GET'])
def form_customers():
     
    return render_template("add_client.html")


@customers_bp.route('/edit/<int:id_customer>', methods=['GET'])
def form_edit_customers(id_customer):
    
    customer = next((u for u in CUSTOMERS if u['id'] == id_customer), None)

    if not customer:
        return "Cliente não encontrado", 404

    return render_template("form_edit_clients.html", customer=customer, edit=True)



"""
    ROTAS DO CRUD DE CLIENTES
"""

@customers_bp.route('/create', methods=['POST'])
def create_customers():

    new_customer = request.form.to_dict()

    print(new_customer)

    if not new_customer:
        return "Dados inconsistentes para cadastro", 400
    
    if new_customer['is_active'] == "true":
        is_active = True
    else:
        is_active = False

    customer_email = is_valid_email(new_customer['email'])
    customer_phone = format_phone(new_customer['phone'])
    customer_cpf = format_cpf(new_customer['cpf'])


    data = {
        "id": len(CUSTOMERS) + 1,
        "name": new_customer['name'],
        "cpf": customer_cpf,
        "phone": customer_phone,
        "email": customer_email,
        "address": new_customer['address'],
        "notes": new_customer['notes'],
        "is_active": is_active
    }

    CUSTOMERS.append(data)

    return redirect(url_for('customers.list_all_customers'))


@customers_bp.route('/update/<int:id_customer>', methods=['POST'])
def update_customers(id_customer):

    customer = next((u for u in CUSTOMERS if u['id'] == id_customer), None)

    if not customer:
        return "Cliente não encontrado", 404

    form = request.form.to_dict()

    updated_email = is_valid_email(form.get('email'))
    updated_phone = format_phone(form.get('phone'))

    customer['name'] = form.get('name')
    customer['phone'] = updated_phone
    customer['email'] = updated_email
    customer['address'] = form.get('address')
    customer['notes'] = form.get('notes')
    customer['is_active'] = form.get('is_active') == "true"

    return redirect(
        url_for(
            'customers.info_customers',
            id_user=id_customer
        )
    )


@customers_bp.route('/del/<int:id_customer>', methods=['POST'])
def delete_customers(id_customer):

    customer = next((u for u in CUSTOMERS if u['id'] == id_customer), None)

    if not customer:
        return "Cliente não encontrado", 404
    
    CUSTOMERS.remove(customer)

    return redirect(url_for('customers.list_all_customers'))

