from dataclasses import dataclass
from typing import Optional
from datetime import date, time

@dataclass
class Event:
    id: str
    name: str
    capacity: int
    description: Optional[str]
    day: date
    start: time
    end: time
    have_certificate: bool