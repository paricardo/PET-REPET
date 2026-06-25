from enum import Enum

class BillingOrigin(str, Enum):
    ONE_TIME = "UMA_VEZ"
    PLAN = "PLANO"