from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from src.core.enums.user_role import UserRole


class UserResponseSchema(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    role: UserRole
    is_active: bool
    created_at: datetime