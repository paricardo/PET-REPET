from peewee import (
    CharField,
    BooleanField
)
from src.models.base_model import BaseModel


class User(BaseModel):

    name = CharField()
    email = CharField(unique=True)
    password_hash = CharField()

    role = CharField(
        default="EMPLOYEE"
    )

    is_active = BooleanField(
        default=True
    )

    class Meta:
        table_name = "users"