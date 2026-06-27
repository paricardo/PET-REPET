from flask import Blueprint, request, jsonify
from src.services.customers_plan_service import CustomerPlanService


customer_plan = Blueprint('customer-plan', __name__)

service = CustomerPlanService()

#------------------------------------
# ROTA QUE LISTA TODOS
#------------------------------------
@customer_plan.route('/', methods=['GET'])
def list_all_customer_plan():

    result = service.get()

    return jsonify(result), 200


#------------------------------------
# ROTA QUE LISTA UM 
#------------------------------------
@customer_plan.route('/<int:id_customer_plan>', methods=['GET'])
def list_customer_plan(id_customer_plan):
    
    result = service.getById(id_customer_plan)

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    
    return jsonify(result), 200



#------------------------------------
# ROTA QUE CRIA UM
#------------------------------------
@customer_plan.route('/', methods=['POST'])
def add_customer_plan():
    
    data = request.get_json()

    result = service.add(data)

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    
    return jsonify(result), 201


#------------------------------------
# ROTA QUE ATUALIZAÇÃO
#------------------------------------
@customer_plan.route('/<int:id_customer_plan>', methods=['PUT'])
def update_customer_plan(id_customer_plan):
    
    data = request.get_json()

    result = service.update(id_customer_plan, data) 

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    
    return jsonify(result), 200


#------------------------------------
# ROTA QUE DELETA
#------------------------------------
@customer_plan.route('/<int:id_customer_plan>', methods=['DELETE'])
def delete_customer_plan(id_customer_plan):
    
    result = service.update(id_customer_plan) 

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    
    return jsonify(result), 200