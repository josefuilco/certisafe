from dataclasses import dataclass
from typing import Optional
from .condition import Condition 
from .faculty import Faculty

@dataclass
class User:
    # Attributes
    id: str
    names: str
    surnames: str
    email: str
    cellphone: str
    dni: str
    # Relations
    condition: Optional[Condition] = None
    faculty: Optional[Faculty] = None
