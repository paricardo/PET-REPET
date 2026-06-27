from pydantic import BaseModel
from datetime import datetime
from src.core.enums.pet_size import PetSize



class PetCreateSchema(BaseModel):
    customer_id: int
    name: str
    breed: str | None = None
    size: PetSize
    notes: str | None = None


class PetUpdateSchema(BaseModel):
    name: str | None = None
    breed: str | None = None
    size: PetSize | None = None
    notes: str | None = None
    is_active: bool | None = None


class PetResponseSchema(BaseModel):
    id: int
    customer_id: int
    name: str
    breed: str | None
    size: PetSize
    notes: str | None
    is_active: bool
    created_at: datetime