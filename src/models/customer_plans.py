from peewee import (
    ForeignKeyField,
    DateTimeField,
    DecimalField,
    CharField
)
from src.models.base_model import BaseModel
from src.models.customers import Customer
from src.models.plans import Plan


class CustomerPlan(BaseModel):

    customer = ForeignKeyField(
        Customer,
        backref="plans"
    )

    plan = ForeignKeyField(
        Plan,
        backref="customers"
    )

    started_at = DateTimeField()

    expires_at = DateTimeField()

    price_paid = DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = CharField(
        default="ACTIVE"
    )

    class Meta:
        table_name = "customer_plans"