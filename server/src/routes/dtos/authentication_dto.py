from pydantic import BaseModel

class AuthenticationDto(BaseModel):
    user_id: str
    role_id: str