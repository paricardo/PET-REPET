import os
from peewee import SqliteDatabase

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

db_path = os.path.join(BASE_DIR, "petshop.db")

db = SqliteDatabase(
    db_path,
    check_same_thread=False
)