from flask import Blueprint, request, jsonify
from src.services.plans_service import PlanService

plan = Blueprint('plan', __name__)

service = PlanService()

#------------------------------------
# ROTA QUE LISTA TODOS OS SERVIÇOS
#------------------------------------
@plan.route('/', methods=['GET'])
def list_all_plans():
    
    result = service.get()

    return jsonify(result), 200

#------------------------------------
# ROTA QUE LISTA UM SERVIÇO
#------------------------------------
@plan.route('/<int:id_service>', methods=['GET'])
def list_plan(id_service):

    result = service.getById(id_service)

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    
    return jsonify(result), 200

#------------------------------------
# ROTA QUE CRIA UM SERVIÇO
#------------------------------------
@plan.route('/', methods=['POST'])
def add_plan():
    
    data = request.get_json()

    result = service.add(data)

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    
    return jsonify(result), 201



#------------------------------------
# ROTA QUE ATUALIZA UM SERVIÇO
#------------------------------------
@plan.route('/int:id_service', methods=['PUT'])
def update_plan(id_plan):
    
    data = request.get_json()

    result = service.update(id_plan, data) 

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    
    return jsonify(result), 200


#------------------------------------
# ROTA QUE DELETA UM SERVIÇO
#------------------------------------
@plan.route('/int:id_plan', methods=['DELETE'])
def delete_service(id_plan):

    result = service.update(id_plan) 

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    
    return jsonify(result), 200