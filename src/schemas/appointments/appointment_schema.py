from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from decimal import Decimal
from src.core.enums.appointment_status import AppointmentStatus
from src.core.enums.billing_origin import BillingOrigin


class AppointmentCreateSchema(BaseModel):
    customer_id: UUID
    pet_id: UUID
    service_id: UUID
    user_id: UUID
    customer_plan_id: UUID | None = None
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
    id: UUID
    customer_id: UUID
    pet_id: UUID
    service_id: UUID
    user_id: UUID
    customer_plan_id: UUID | None

    scheduled_at: datetime
    billing_origin: BillingOrigin
    final_price: Decimal

    status: AppointmentStatus
    notes: str | None

    created_at: datetime