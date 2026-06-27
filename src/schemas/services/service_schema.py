from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel


class ServiceCreateSchema(BaseModel):
    name: str
    description: str | None = None
    price_small: Decimal
    price_medium: Decimal
    price_large: Decimal


class ServiceUpdateSchema(BaseModel):
    name: str | None = None
    description: str | None = None
    price_small: Decimal | None = None
    price_medium: Decimal | None = None
    price_large: Decimal | None = None
    is_active: bool | None = None


class ServiceResponseSchema(BaseModel):
    id: int
    name: str
    description: str | None
    price_small: Decimal
    price_medium: Decimal
    price_large: Decimal
    is_active: bool
    created_at: datetime