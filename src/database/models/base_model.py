import uuid
from peewee import Model, CharField, DateTimeField
from datetime import datetime
from src.database.connection import db


class BaseModel(Model):

    id = CharField(
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    created_at = DateTimeField(
        default=datetime.now
    )

    class Meta:
        database = db