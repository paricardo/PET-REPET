from peewee import (
    CharField,
    TextField,
    DecimalField,
    BooleanField
)
from src.database.models.base_model import BaseModel


class Service(BaseModel):

    name = CharField()

    description = TextField(
        null=True
    )

    price_small = DecimalField(
        max_digits=10,
        decimal_places=2
    )

    price_medium = DecimalField(
        max_digits=10,
        decimal_places=2
    )

    price_large = DecimalField(
        max_digits=10,
        decimal_places=2
    )

    is_active = BooleanField(
        default=True
    )

    class Meta:
        table_name = "services"