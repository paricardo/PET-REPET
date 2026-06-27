from flask import Blueprint, request, jsonify
from src.services.services_service import ServiceService

service_route = Blueprint('service', __name__)

service = ServiceService()

#------------------------------------
# ROTA QUE LISTA TODOS OS SERVIÇOS
#------------------------------------
@service_route.route('/', methods=['GET'])
def list_all_services():
    
    result = service.get()

    return jsonify(result), 200

#------------------------------------
# ROTA QUE LISTA UM SERVIÇO
#------------------------------------
@service_route.route('/<int:id_service>', methods=['GET'])
def list_service(id_service: int):

    result = service.getById(id_service)

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    
    return jsonify(result), 200

#------------------------------------
# ROTA QUE CRIA UM SERVIÇO
#------------------------------------
@service_route.route('/', methods=['POST'])
def add_service():
    
    data = request.get_json()

    result = service.add(data)

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    
    return jsonify(result), 201



#------------------------------------
# ROTA QUE ATUALIZA UM SERVIÇO
#------------------------------------
@service_route.route('/<int:id_service>', methods=['PUT'])
def update_service(id_service: int):
    
    data = request.get_json()

    result = service.update(id_service, data) 

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    
    return jsonify(result), 200


#------------------------------------
# ROTA QUE DELETA UM SERVIÇO
#------------------------------------
@service_route.route('/<int:id_service>', methods=['DELETE'])
def delete_service(id_service: int):

    result = service.delete(id_service) 

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    
    return jsonify(result), 200