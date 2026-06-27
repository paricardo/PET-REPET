from uuid import UUID 
from src.database.models.appointments import Appointment
from src.schemas.appointments.appointment_schema import *


class AppointmentService:

    def get():
        
        appointments = Appointment.select()

        return [
            AppointmentResponseSchema.model_validate(appointment)
            for appointment in appointments
        ]


    def getById(id_appointment: int):

        appointments = Appointment.get_or_none(
            Appointment.id == UUID(id_appointment)
        )

        if not appointments:
            raise ValueError("Agendamento não encontrado.")

        return AppointmentResponseSchema.model_validate(
            appointments
        )


    
    def add(data):

        appointment_data = AppointmentCreateSchema(**data)

        appointment = Appointment.create(
            customer_id=appointment_data.customer_id,
            pet_id=appointment_data.pet_id,
            service_id=appointment_data.service_id,
            user_id=appointment_data.user_id,
            customer_plan_id=appointment_data.customer_plan_id,
            scheduled_at=appointment_data.scheduled_at,
            billing_origin=appointment_data.billing_origin,
            final_price=appointment_data.final_price,
            notes=appointment_data.notes
        )

        return AppointmentResponseSchema.model_validate(
            appointment
        ).model_dump()


    def update(id_appointment: int, data):
    
        appointment = Appointment.get_or_none(Appointment.id == id_appointment)

        if not appointment:
            return {"error": "Agendamento não encontrado"}, 404
        
        appointment_data = AppointmentUpdateSchema(**data)
        update_data = appointment_data.model_dump(exclude_unset=True)

        Appointment.update(**update_data).where(Appointment.id == id_appointment).execute()

        appointment = Appointment.get(Appointment.id == id_appointment)

        return AppointmentResponseSchema(
            id=update_data.id,
            customer_id=update_data.customer_id,
            pet_id=update_data.pet_id,
            service_id=update_data.service_id,
            user_id=update_data.user_id,
            customer_plan_id=update_data.customer_plan_id,
            scheduled_at=update_data.scheduled_at,
            billing_origin=update_data.billing_origin,
            final_price=update_data.final_price,
            status=update_data.status,
            notes=update_data.notes,
            created_at=update_data.created_at
        ).model_dump()


    def delete(id_appointment: int):
        
        appointment = Appointment.get_or_none(Appointment.id == id_appointment)

        if not appointment:
            return {"error": "Agendamento não encontrado"}, 404
        
        appointment.delete_instance()

        return {"message": "Agendamento removido com sucesso"}, 200