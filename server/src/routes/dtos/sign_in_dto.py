from pydantic import BaseModel, Field

class SignInDto(BaseModel):
    dni: str = Field(title='DNI del usuario', max_length=8, min_length=8)
    password: str = Field(title='Contraseña del usuario', max_length=24, min_length=8)