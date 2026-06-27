from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel
from src.core.enums.plan_status import PlanStatus


class CustomerPlanCreateSchema(BaseModel):
    customer_id: int
    plan_id: int
    started_at: datetime
    price_paid: Decimal


class CustomerPlanUpdateSchema(BaseModel):
    status: PlanStatus | None = None
    expires_at: datetime | None = None


class CustomerPlanResponseSchema(BaseModel):
    id: int
    customer_id: int
    plan_id: int
    started_at: datetime
    expires_at: datetime
    price_paid: Decimal
    status: PlanStatus
    created_at: datetime