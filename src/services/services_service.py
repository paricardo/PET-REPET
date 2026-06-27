from src.database.models.services import Service
from src.schemas.services.service_schema import *


class ServiceService:

    def get():
        
        services = Service.select()

        return [
            ServiceResponseSchema.model_validate(services)
            for service in services
        ]


    def getById(id_service: int):

        service = Service.get_or_none(
            Service.id == UUID(id_service)
        )

        if not service:
            raise ValueError("Serviço não encontrado.")

        return ServiceResponseSchema.model_validate(
            service
        )


    
    def add(data):

        service_data = ServiceCreateSchema(**data)

        service = Service.create(
            name=service_data.name,
            description=service_data.description,
            price_small=service_data.price_small,
            price_medium=service_data.price_medium,
            price_large=service_data.price_large
        )

        return ServiceResponseSchema.model_validate(
            service
        ).model_dump()


    def update(id_service: int, data):
    
        service = Service.get_or_none(Service.id == id_service)

        if not service:
            return {"error": "Serviço não encontrado"}, 404
        
        service_data = ServiceUpdateSchema(**data)
        update_data = service_data.model_dump(exclude_unset=True)

        Service.update(**update_data).where(Service.id == id_service).execute()

        service = Service.get(Service.id == id_service)

        return ServiceResponseSchema(
            id=service.id,
            name=service.name,
            description=service.description,
            price_small=service.price_small,
            price_medium=service.price_medium,
            price_large=service.price_large,
            is_active=service.is_active,
            created_at=service.created_at
        ).model_dump()


    def delete(id_service: int):
        
        service = Service.get_or_none(Service.id == id_service)

        if not service:
            return {"error": "Serviço não encontrado"}, 404
        
        service.delete_instance()

        return {"message": "Service removido com sucesso"}, 200