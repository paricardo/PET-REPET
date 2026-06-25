from database.connection import db

from src.database.models.users import User
from src.database.models.customers import Customer
from src.database.models.pets import Pet
from src.database.models.services import Service
from src.database.models.plans import Plan
from src.database.models.customer_plans import CustomerPlan
from src.database.models.appointments import Appointment


def create_tables():
    db.connect()

    db.create_tables([
        User,
        Customer,
        Pet,
        Service,
        Plan,
        CustomerPlan,
        Appointment
    ])

    db.close()


if __name__ == "__main__":
    create_tables()