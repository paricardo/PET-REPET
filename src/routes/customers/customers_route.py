from flask import Blueprint, jsonify, request
from src.services.customers_service import CustomerService

service = CustomerService()

customers = Blueprint("customers", __name__)

#---------------------------------------
# ROTA QUE LISTA TODOS OS CLIENTES
#---------------------------------------
@customers.route('/', methods=["GET"])
def list_all_customers():
    
    result = service.get()

    return jsonify(result), 200


#---------------------------------------
# ROTA QUE LISTA UM CLIENTE PELO ID
#---------------------------------------
@customers.route('/<int:id_customer>', methods=["GET"])
def list_customer(id_customer):

    result = service.get_by_id(id_customer)

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]

    return jsonify(result), 200

#---------------------------------------
# ROTA QUE CRIA UM CLIENTE NO BANCO
#---------------------------------------
@customers.route('/', methods=["POST"])
def add_customers():
    data = request.get_json()

    result = service.create(data)
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    return jsonify(result), 201


#---------------------------------------
# ROTA QUE ATUALIZA O CLIENTE NO BANCO
#---------------------------------------
@customers.route('/<int:id_customer>', methods=["PUT"])
def update_customer(id_customer):

    result = service.update(id_customer)

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    return jsonify(result), 201


#---------------------------------------
# ROTA QUE DELETA UM USUARIO DO BANCO
#---------------------------------------
@customers.route('/<int:id_customer>', methods=["DELETE"])
def delete_customer(id_customer):

    result = service.delete(id_customer)

    if isinstance(result, tuple):
        return jsonify(result[0], result[1])
    
    return jsonify(result), 200

@customers.route('/<int:id_customer>', methods=["POST"])
def activate(self, id_customer):
    pass

@customers.route('/<int:id_customer>', methods=["POST"])
def deactivate(self, id_customer):
    pass