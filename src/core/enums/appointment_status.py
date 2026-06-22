from enum import Enum

class AppointmentStatus(str, Enum):
    SCHEDULED = "AGENDADO"
    COMPLETED = "COMPLETO"
    CANCELED = "CANCELADO"