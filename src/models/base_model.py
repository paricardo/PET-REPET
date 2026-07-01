from peewee import Model, AutoField, DateTimeField
from datetime import datetime
from src.database.connection import db


class BaseModel(Model):

    id = AutoField()

    created_at = DateTimeField(
        default=datetime.now
    )

    class Meta:
        database = db