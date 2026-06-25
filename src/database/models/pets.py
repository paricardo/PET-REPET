from peewee import (
    ForeignKeyField,
    CharField,
    TextField,
    BooleanField
)
from src.database.models.base_model import BaseModel
from src.database.models.customers import Customer


class Pet(BaseModel):

    customer = ForeignKeyField(
        Customer,
        backref="pets",
        on_delete="CASCADE"
    )

    name = CharField()

    breed = CharField(
        null=True
    )

    size = CharField()

    notes = TextField(
        null=True
    )

    is_active = BooleanField(
        default=True
    )

    class Meta:
        table_name = "pets"