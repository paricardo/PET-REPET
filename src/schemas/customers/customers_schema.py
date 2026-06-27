from datetime import datetime
from pydantic import BaseModel, EmailStr


class CustomerCreateSchema(BaseModel):
    name: str
    phone: str
    email: EmailStr | None = None
    notes: str | None = None


class CustomerUpdateSchema(BaseModel):
    name: str | None = None
    phone: str | None = None
    email: EmailStr | None = None
    notes: str | None = None
    is_active: bool | None = None


class CustomerResponseSchema(BaseModel):
    id: int
    name: str
    phone: str
    email: str | None
    notes: str | None
    is_active: bool
    created_at: datetime