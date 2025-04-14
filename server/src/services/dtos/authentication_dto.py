from dataclasses import dataclass

@dataclass
class AuthenticationDto:
    user_id: str
    role_id: int