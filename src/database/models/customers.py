from peewee import (
    CharField,
    TextField,
    BooleanField
)
from src.database.models.base_model import BaseModel


class Customer(BaseModel):

    name = CharField()
    phone = CharField()

    email = CharField(
        null=True
    )

    notes = TextField(
        null=True
    )

    is_active = BooleanField(
        default=True
    )

    class Meta:
        table_name = "customers"