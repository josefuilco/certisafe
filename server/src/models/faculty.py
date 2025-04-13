from dataclasses import dataclass
from typing import Optional

@dataclass
class Faculty:
    id: int
    name: Optional[str] = None