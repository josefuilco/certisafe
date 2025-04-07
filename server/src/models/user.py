from dataclasses import dataclass
from .condition import Condition 
from .faculty import Faculty

@dataclass
class User:
    # Attributes
    names: str
    surnames: str
    email: str
    cellphone: str
    dni: str
    # Relations
    condition: Condition
    faculty: Faculty
