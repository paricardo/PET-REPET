from src.schemas.pets.pet_schema import *
from src.database.models.pets import Pet

class PetService:
    # LISTA TODOS
    def get(self):
        
        pets = Pet.select()

        return [
            PetResponseSchema(
                id=pet.id,
                customer_id=pet.customers_id,
                name=pet.name,
                breed=pet.breed,
                size=pet.size,
                notes=pet.notes,
                is_active=pet.is_active,
                created_at=pet.created_at
            ).model_dump()
            for pet in pets
        ]


    # LISTA UM
    def getById(self, id_pet: int):
        
        pet = Pet.get_or_none(Pet.id == id_pet)

        if not pet:
            return {"error": "Pet não encontrado"}, 404
        
        return PetResponseSchema(
            id=pet.id,
            customer_id=pet.customers_id,
            name=pet.name,
            breed=pet.breed,
            size=pet.size,
            notes=pet.notes,
            is_active=pet.is_active,
            created_at=pet.created_at
        ).model_dump()

    # ADD PETS
    def add(self, data):
        pet_data = PetCreateSchema(**data)

        pet = Pet.create(
            customer_id=pet_data.customer_id,
            name=pet_data.name,
            breed=pet_data.breed,
            size=pet_data.size,
            notes=pet_data.notes
        )

        return PetResponseSchema.model_validate(
            pet
        ).model_dump()



    # UPDATE PETS
    def update(self, id_pet: int, data):
        
        pet = Pet.get_or_none(Pet.id == id_pet)

        if not pet:
            return {"error": "Pet não encontrado"}, 404
        
        pet_data = PetUpdateSchema(**data)
        update_data = pet_data.model_dump(exclude_unset=True)

        Pet.update(**update_data).where(Pet.id == id_pet).execute()

        pet = Pet.get(Pet.id == id_pet)

        return PetResponseSchema(
            id=pet.id,
            customer_id=pet.customer_id,
            name=pet.name,
            breed=pet.breed,
            size=pet.size,
            notes=pet.notes,
            is_active=pet.is_active,
            created_at=pet.created_at
        ).model_dump()



    
    # DELETE PETS
    def delete(self, id_pet: int):
        
        pet = Pet.get_or_none(Pet.id == id_pet)

        if not pet:
            return {"error": "Pet não encontrado"}, 404
        
        pet.delete_instance()

        return {"message": "Pet removido com sucesso"}, 200
    




    def activate(self, id_pet: int):
        pass

    def deactivate(self, id_pet: int):
        pass