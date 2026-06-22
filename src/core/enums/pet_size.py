from enum import Enum 


class PetSize(str, Enum):
    SMALL = "PEQUENO"
    MEDIUM = "MÉDIO"
    LARGE = "GRANDE"