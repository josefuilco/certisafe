from dataclasses import dataclass
from typing import Optional

@dataclass
class Condition:
    id: int
    name: Optional[str] = None