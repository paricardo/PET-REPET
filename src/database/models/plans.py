from peewee import (
    CharField,
    TextField,
    IntegerField,
    DecimalField,
    BooleanField
)
from src.database.models.base_model import BaseModel

class Plan(BaseModel):

    name = CharField()

    description = TextField(
        null=True
    )

    price = DecimalField(
        max_digits=10,
        decimal_places=2
    )

    duration_days = IntegerField()

    services_info = TextField()

    is_active = BooleanField(
        default=True
    )

    class Meta:
        table_name = "plans"