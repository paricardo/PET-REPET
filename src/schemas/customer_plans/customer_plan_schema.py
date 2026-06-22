from datetime import datetime
from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel
from src.core.enums.plan_status import PlanStatus


class CustomerPlanCreateSchema(BaseModel):
    customer_id: UUID
    plan_id: UUID
    started_at: datetime
    price_paid: Decimal


class CustomerPlanUpdateSchema(BaseModel):
    status: PlanStatus | None = None
    expires_at: datetime | None = None


class CustomerPlanResponseSchema(BaseModel):
    id: UUID
    customer_id: UUID
    plan_id: UUID
    started_at: datetime
    expires_at: datetime
    price_paid: Decimal
    status: PlanStatus
    created_at: datetime