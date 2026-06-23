import bcrypt
from flask_jwt_extended import create_access_token
from uuid import uuid4
from datetime import datetime, timezone

from src.core.enums.user_role import UserRole
from src.database.models.users import User


class AuthService:

    def login(self, email, password):

        user = User.get_or_none(User.email == email)

        if not user:
            return {"error": "usuário não encontrado"}, 401

        password_is_valid = bcrypt.checkpw(
            password.encode("utf-8"),
            user.password_hash.encode("utf-8")
        )

        if not password_is_valid:
            return {"error": "senha inválida"}, 401

        token = create_access_token(
            identity=str(user.id),
            additional_claims={
                "role": user.role
            }
        )

        return {
            "access_token": token,
            "user": {
                "id": user.id,
                "email": user.email,
                "role": user.role
            }
        }, 200

    def register(self, name, email, password):

        # 1. Verificar se já existe usuário
        existing_user = User.get_or_none(User.email == email)

        if existing_user:
            return {"error": "usuário já existe"}, 409

        # 2. Hash da senha
        password_hash = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        # 3. Criar usuário
        user = User.create(
            id=str(uuid4()),
            name=name,
            email=email,
            password_hash=password_hash,  # 🔥 TEM QUE SER ESSE NOME
            role=UserRole.EMPLOYEE,
            is_active=True,
            created_at=datetime.now(timezone.utc)
        )

        return {
            "message": "usuário criado com sucesso",
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "role": user.role
            }
        }, 201