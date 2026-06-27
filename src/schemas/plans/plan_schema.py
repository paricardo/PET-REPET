from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel


class PlanCreateSchema(BaseModel):
    name: str
    description: str | None = None
    price: Decimal
    duration_days: int
    services_info: str


class PlanUpdateSchema(BaseModel):
    name: str | None = None
    description: str | None = None
    price: Decimal | None = None
    duration_days: int | None = None
    services_info: str | None = None
    is_active: bool | None = None


class PlanResponseSchema(BaseModel):
    id: int
    name: str
    description: str | None
    price: Decimal
    duration_days: int
    services_info: str
    is_active: bool
    created_at: datetime
    