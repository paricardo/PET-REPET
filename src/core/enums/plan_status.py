from enum import Enum

class PlanStatus(str, Enum):
    ACTIVE = "ATIVO"
    EXPIRED = "EXPIRADO"
    CANCELED = "CANCELADO"