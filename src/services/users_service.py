import bcrypt
from datetime import datetime, timezone
from uuid import uuid4

from src.database.models.users import User
from src.schemas.users.user_schema import *
from src.core.enums.user_role import UserRole


class UserService:

    # ---------------------------
    # helper
    # ---------------------------
    def get_user_entity(self, user_id):
        return User.get_or_none(User.id == user_id)

    # ---------------------------
    # CREATE
    # ---------------------------
    def add(self, data, current_user=None):

        user_data = UserCreateSchema(**data)

        role = UserRole.EMPLOYEE

        if current_user and current_user.role == UserRole.ADMIN:
            role = user_data.role or UserRole.EMPLOYEE

        password_hash = bcrypt.hashpw(
            user_data.password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        user = User.create(
            id=str(uuid4()),
            name=user_data.name,
            email=user_data.email,
            password_hash=password_hash,
            role=role,
            is_active=True,
            created_at=datetime.now(timezone.utc)
        )

        return UserResponseSchema(
            id=user.id,
            name=user.name,
            email=user.email,
            role=user.role,
            is_active=user.is_active,
            created_at=user.created_at
        ).model_dump()

    # ---------------------------
    # GET ALL
    # ---------------------------
    def get(self):
        users = User.select()

        return [
            UserResponseSchema(
                id=user.id,
                name=user.name,
                email=user.email,
                role=user.role,
                is_active=user.is_active,
                created_at=user.created_at
            ).model_dump()
            for user in users
        ]

    # ---------------------------
    # GET BY ID
    # ---------------------------
    def getById(self, id_user):

        user = User.get_or_none(User.id == id_user)

        if not user:
            return {"error": "usuário não encontrado"}, 404

        return UserResponseSchema(
            id=user.id,
            name=user.name,
            email=user.email,
            role=user.role,
            is_active=user.is_active,
            created_at=user.created_at
        ).model_dump()

    # ---------------------------
    # UPDATE
    # ---------------------------
    def update(self, id_user, **data):

        user = User.get_or_none(User.id == id_user)

        if not user:
            return {"error": "usuário não encontrado"}, 404

        user_data = UserUpdateSchema(**data)
        update_data = user_data.model_dump(exclude_unset=True)

        if "password" in update_data:
            update_data["password_hash"] = bcrypt.hashpw(
                update_data["password_hash"].encode("utf-8"),
                bcrypt.gensalt()
            ).decode("utf-8")

        User.update(**update_data).where(User.id == id_user).execute()

        user = User.get(User.id == id_user)

        return UserResponseSchema(
            id=user.id,
            name=user.name,
            email=user.email,
            role=user.role,
            is_active=user.is_active,
            created_at=user.created_at
        ).model_dump()

    # ---------------------------
    # DELETE
    # ---------------------------
    def delete(self, id_user):

        user = User.get_or_none(User.id == id_user)

        if not user:
            return {"error": "usuário não encontrado"}, 404

        user.delete_instance()

        return {"message": "Usuário removido com sucesso"}