from pydantic import BaseModel, EmailStr, Field

class CreateUserDto(BaseModel):
    names: str = Field(description="Names of the user", max_length=25, min_length=1)
    surnames: str = Field(description="Surnames of the user", max_length=25, min_length=1)
    email: EmailStr = Field(description="Email of the user", max_length=50, min_length=1)
    cellphone: str = Field(description="Cellphone Number of the user", max_length=9, min_length=9, pattern=r"^\d{9}$")
    dni: str = Field(description="DNI of the user", max_length=8, min_length=8, pattern=r"^\d{8}$")
    faculty: int = Field(description="Faculty of the user")
    condition: int = Field(description="Condition of the user")