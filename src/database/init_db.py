from database.connection import db

from src.models.users import User
from src.models.customers import Customer
from src.models.pets import Pet
from src.models.services import Service
from src.models.plans import Plan
from src.models.customer_plans import CustomerPlan
from src.models.appointments import Appointment


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