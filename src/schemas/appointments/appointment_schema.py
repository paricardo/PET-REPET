from datetime import datetime
from pydantic import BaseModel
from decimal import Decimal
from src.core.enums.appointment_status import AppointmentStatus
from src.core.enums.billing_origin import BillingOrigin


class AppointmentCreateSchema(BaseModel):
    customer_id: int
    pet_id: int
    service_id: int
    user_id: int
    customer_plan_id: int | None = None
    scheduled_at: datetime
    billing_origin: BillingOrigin
    final_price: Decimal
    notes: str | None = None


class AppointmentUpdateSchema(BaseModel):
    scheduled_at: datetime | None = None
    status: AppointmentStatus | None = None
    final_price: Decimal | None = None
    notes: str | None = None


class AppointmentResponseSchema(BaseModel):
    id: int
    customer_id: int
    pet_id: int
    service_id: int
    user_id: int
    customer_plan_id: int | None

    scheduled_at: datetime
    billing_origin: BillingOrigin
    final_price: Decimal

    status: AppointmentStatus
    notes: str | None

    created_at: datetime