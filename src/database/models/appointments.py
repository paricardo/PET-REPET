from peewee import (
    ForeignKeyField,
    CharField,
    TextField,
    DateTimeField,
    DecimalField
)

from src.database.models.base_model import BaseModel
from src.database.models.customers import Customer
from src.database.models.pets import Pet
from src.database.models.services import Service
from src.database.models.users import User
from src.database.models.customer_plans import CustomerPlan


class Appointment(BaseModel):

    customer = ForeignKeyField(
        Customer,
        backref="appointments"
    )

    pet = ForeignKeyField(
        Pet,
        backref="appointments"
    )

    service = ForeignKeyField(
        Service,
        backref="appointments"
    )

    user = ForeignKeyField(
        User,
        backref="appointments"
    )

    customer_plan = ForeignKeyField(
        CustomerPlan,
        backref="appointments",
        null=True
    )

    scheduled_at = DateTimeField()

    billing_origin = CharField()

    final_price = DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = CharField(
        default="SCHEDULED"
    )

    notes = TextField(
        null=True
    )

    class Meta:
        table_name = "appointments"