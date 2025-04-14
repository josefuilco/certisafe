from dataclasses import dataclass
from typing import Optional

@dataclass
class Account:
    dni: str
    password: str
    role_id: Optional[int] = None