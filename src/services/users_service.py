import bcrypt
from datetime import datetime, timezone
from src.schemas.users.user_create_schema import UserCreateSchema
from src.schemas.users.user_response_schema import UserResponseSchema
from src.schemas.users.user_update_schema import UserUpdateSchema
from src.core.enums.user_role import UserRole
from src.database.in_memory.db_in_memory import USERS
from uuid import uuid4

class UserService:

    # Serviço para adicionar usuários
    def add(self, data, current_user=None):

        # valida schema antes (já feito na rota)
        user_data = UserCreateSchema(**data)

        # REGRA DE NEGÓCIO (role controlado aqui)
        role = UserRole.EMPLOYEE

        # se quem está criando for admin, pode escolher role
        if current_user and current_user.role == UserRole.ADMIN:
            role = user_data.role or UserRole.EMPLOYEE

        #Hash da senha 
        password_hash = bcrypt.hashpw(
            user_data.password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")


        user = {
            "id": str(uuid4()),
            "name": user_data.name,
            "email": user_data.email,
            "password_hash": password_hash,
            "role": role,
            "is_active": True,
            "created_at": datetime.now(timezone.utc)
        }

        USERS.append(user)

        return UserResponseSchema(
            id=user["id"],
            name=user["name"],
            email=user["email"],
            role=user["role"],
            is_active=user["is_active"],
            created_at=user["created_at"]
        ).model_dump()
    

    #Serviço para listar todos os usuários
    def get(self):
        return [
            UserResponseSchema (
                id=user["id"],
                name=user["name"],
                email=user["email"],
                role=user["role"],
                is_active=user["is_active"],
                created_at=user["created_at"]
            ).model_dump()
            for user in USERS
        ]


    #Serviço que lista um Usuário
    def getById(self, id_user):
        for user in USERS:
            if user["id"] == id_user:
                return user
        

    # Update de usuários
    def update(self, id_user, **data):
        
        user_data = UserUpdateSchema(**data)

        for user in USERS:

            if user["id"] == id_user:

                update_data = user_data.model_dump(exclude_unset=True)

                user.update(update_data)

                return UserResponseSchema(**user).model_dump()

        return None


    # Serviço que deleta o usuário
    def delete(self, id_user):

        for user in USERS:

            if user["id"] == id_user:
                USERS.remove(user)

                return {
                    "message": "Usuário removido com sucesso"
                }

        return None