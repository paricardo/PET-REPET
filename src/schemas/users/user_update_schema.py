from pydantic import BaseModel
from typing import Optional
from src.core.enums.user_role import UserRole

class UserUpdateSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    role: Optional[UserRole] = None
    is_active: Optional[bool] = None