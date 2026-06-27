from flask import Blueprint, request, jsonify
from src.services.appointment_service import AppointmentService

appointment = Blueprint('service', __name__)


service = AppointmentService()

#------------------------------------
# ROTA QUE LISTA TODOS OS AGENDAMENTOS
#------------------------------------
@appointment.route('/', methods=['GET'])
def list_all_appointments():
    
    result = service.get()

    return jsonify(result), 200

#------------------------------------
# ROTA QUE LISTA UM SERVIÇO
#------------------------------------
@appointment.route('/<int:id_appointment>', methods=['GET'])
def list_appointment(id_appointment):

    result = service.getById(id_appointment)

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    
    return jsonify(result), 200

#------------------------------------
# ROTA QUE CRIA UM SERVIÇO
#------------------------------------
@appointment.route('/', methods=['POST'])
def add_appointment():
    
    data = request.get_json()

    result = service.add(data)

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    
    return jsonify(result), 201



#------------------------------------
# ROTA QUE ATUALIZA UM SERVIÇO
#------------------------------------
@appointment.route('/int:id_appointment', methods=['PUT'])
def update_appointment(id_appointment):
    
    data = request.get_json()

    result = service.update(id_appointment, data) 

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    
    return jsonify(result), 200


#------------------------------------
# ROTA QUE DELETA UM SERVIÇO
#------------------------------------
@appointment.route('/int:id_appointment', methods=['DELETE'])
def delete_appointment(id_appointment):

    result = service.update(id_appointment) 

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    
    return jsonify(result), 200