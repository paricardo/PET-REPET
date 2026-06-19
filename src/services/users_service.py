from src.schemas.users.user_create_schema import UserCreateSchema
from werkzeug.security import generate_password_hash
from src.core.enums.user_role import UserRole
from src.database.in_memory.db_in_memory import USERS
from uuid import uuid4

class UserService:

    def add(self, data, current_user=None):

        # valida schema antes (já feito na rota)
        user_data = UserCreateSchema(**data)

        # 🔐 REGRA DE NEGÓCIO (role controlado aqui)
        role = UserRole.EMPLOYEE

        # se quem está criando for admin, pode escolher role
        if current_user and current_user.role == UserRole.ADMIN:
            role = user_data.role or UserRole.EMPLOYEE

        user = {
            "id": uuid4(),
            "name": user_data.name,
            "email": user_data.email,
            "password_hash": generate_password_hash(user_data.password),
            "role": role 
        }

        USERS.append(user)

        return USERS

    def get():
        pass


    def getById():
        pass


    def edit():
        pass


    def delete():
        pass
