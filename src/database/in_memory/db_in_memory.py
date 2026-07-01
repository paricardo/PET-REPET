from datetime import datetime

#1
USERS = [
    {
        "id": 1, 
        "name": "Paulo", 
        "email": "paulo@email.com", 
        "password_hash": "teste@123",
        "role": "ADMIN",
        "is_active": True,
        "created_at": datetime.now()
    }
]

#2
CUSTOMERS = [
    {
        "id": 1, 
        "name": "Carlos", 
        "phone": "(62) 9999-8888",
        "email": "carlos@email.com", 
        "address": "Rua zacarias alves lima q.76 lt.12 jardim dom bosco",
        "notes": "teste de cliente",
        "is_active": True,
        "created_at": datetime.now()
    }
]

#3
PETS = []

#4
SERVICES = []

#5
PLANS = []

#6
CUSTOMERS_PLANS = []

#7
APPOINTMENTS = []