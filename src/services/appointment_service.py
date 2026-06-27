from src.database.models.appointments import Appointment
from src.schemas.appointments.appointment_schema import *


class AppointmentService:

    def get(self):
        
        appointments = Appointment.select()

        return [
            AppointmentResponseSchema.model_validate(appointment).model_dump()
            for appointment in appointments
        ]


    def getById(self, id_appointment: int):

        appointment = Appointment.get_or_none(
            Appointment.id == id_appointment
        )

        if not appointment:
            return {"error": "Agendamento não encontrado."}, 404

        return AppointmentResponseSchema(
            id=appointment.id,
            customer_id=appointment.customer_id,
            pet_id=appointment.pet_id,
            service_id=appointment.service_id,
            user_id=appointment.user_id,
            customer_plan_id=appointment.customer_plan_id,
            scheduled_at=appointment.scheduled_at,
            billing_origin=appointment.billing_origin,
            final_price=appointment.final_price,
            status=appointment.status,
            notes=appointment.notes,
            created_at=appointment.created_at
        ).model_dump()


    
    def add(self, data):

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


    def update(self, id_appointment: int, data):
    
        appointment = Appointment.get_or_none(Appointment.id == id_appointment)

        if not appointment:
            return {"error": "Agendamento não encontrado"}, 404
        
        appointment_data = AppointmentUpdateSchema(**data)
        update_data = appointment_data.model_dump(exclude_unset=True)

        Appointment.update(**update_data).where(Appointment.id == id_appointment).execute()

        appointment = Appointment.get(Appointment.id == id_appointment)

        return AppointmentResponseSchema(
            id=appointment.id,
            customer_id=appointment.customer_id,
            pet_id=appointment.pet_id,
            service_id=appointment.service_id,
            user_id=appointment.user_id,
            customer_plan_id=appointment.customer_plan_id,
            scheduled_at=appointment.scheduled_at,
            billing_origin=appointment.billing_origin,
            final_price=appointment.final_price,
            status=appointment.status,
            notes=appointment.notes,
            created_at=appointment.created_at
        ).model_dump()


    def delete(self, id_appointment: int):
        
        appointment = Appointment.get_or_none(Appointment.id == id_appointment)

        if not appointment:
            return {"error": "Agendamento não encontrado"}, 404
        
        appointment.delete_instance()

        return {"message": "Agendamento removido com sucesso"}, 200