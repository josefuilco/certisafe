from dataclasses import dataclass
from .event import Event

@dataclass
class EventsByUser(Event):
    is_registered: bool