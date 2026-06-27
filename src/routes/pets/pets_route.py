from flask import Blueprint, request, jsonify
from src.services.pets_service import PetService


pets = Blueprint('pets',  __name__)

service = PetService()


#------------------------------------
# ROTA QUE LISTA TODOS OS USUÁRIOS DO BANCO
#------------------------------------
@pets.route('/', methods=['GET'])
def list_all_pets():
    
    result = service.get()

    return jsonify(result), 200


#------------------------------------
# ROTA QUE LISTA UM USUÁRIO
#------------------------------------
@pets.route('/<int:id_pet>', methods=['GET'])
def list_pet(id_pet: int):
    
    result = service.getById(id_pet)

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]

    return jsonify(result), 200

#------------------------------------
# ROTA QUE CRIA UM PET NO BANCO
#------------------------------------
@pets.route('/', methods=['POST'])
def add_pet():

    data = request.get_json()

    result = service.add(data)

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    
    return jsonify(result), 201


#------------------------------------
# ROTA QUE ATUALIZA UM PET NO BANCO
#------------------------------------
@pets.route('/<int:id_pet>', methods=['PUT'])
def update_pet(id_pet: int):

    data = request.get_json()

    result = service.update(id_pet, data)

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    
    return jsonify(result), 200

#------------------------------------
# ROTA QUE DELETA UM PET NO BANCO
#------------------------------------
@pets.route('/<int:id_pet>', methods=['DELETE'])
def delete_pet(id_pet: int):

    result = service.delete(id_pet)

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    
    return jsonify(result), 200