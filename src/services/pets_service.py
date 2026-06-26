from src.schemas.pets.pet_schema import *
from src.database.models.pets import Pet

class PetService:
    # LISTA TODOS
    def get():
        
        pets = Pet.select()

        return [
            PetResponseSchema(
                id=pets.id,
                customer=pets.customers_id,
                name=pets.name,
                breed=pets.breed,
                size=pets.size,
                notes=pets.notes,
                is_active=pets.is_active,
                created_at=pets.created_at
            ).model_dump()
            for pet in pets
        ]


    # LISTA UM
    def getById(id_pet: int):
        
        pet = Pet.get_or_none(Pet.id == id_pet)

        if not pet:
            return {"error": "Pet não encontrado"}, 404
        
        return PetResponseSchema(
            id=pet.id,
            customer=pet.customers_id,
            name=pet.name,
            breed=pet.breed,
            size=pet.size,
            notes=pet.notes,
            is_active=pet.is_active,
            created_at=pet.created_at
        ).model_dump()

    # ADD PETS
    def add(data):
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
    def update(id_pet: int, data):
        
        pet = Pet.get_or_none(Pet.id == id_pet)

        if not pet:
            return {"error": "Pet não encontrado"}, 404
        
        pet_data = PetUpdateSchema(**data)
        update_data = pet_data.model_dump(exclude_unset=True)

        Pet.update(**update_data).where(Pet.id == id_pet).execute()

        pet = pet.get(pet.id == id_pet)

        return PetResponseSchema(
            id=pet.id,
            name=pet.name,
            phone=pet.phone,
            email=pet.email,
            notes=pet.notes,
            is_active=pet.is_active,
            created_at=pet.created_at
        ).model_dump()



    
    # DELETE PETS
    def delete(id_pet: int):
        
        pet = Pet.get_or_none(Pet.id == id_pet)

        if not pet:
            return {"error": "Pet não encontrado"}, 404
        
        pet.delete_instance()

        return {"error": "Pet removido com sucessso"}
    




    def activate(self, id_pet: int):
        pass

    def deactivate(self, id_pet: int):
        pass