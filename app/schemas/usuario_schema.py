
from pydantic import BaseModel, EmailStr


# Schema base: campos comuns entre entrada e saída
class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    senha: str


# Schema para criação (entrada)
class UsuarioCreate(UsuarioBase):
    pass  # Herda tudo de UsuarioBase


# Schema para leitura (saída)
class UsuarioRead(UsuarioBase):
    id: int

    class Config:
        orm_mode = True  # Necessário para converter objetos SQLAlchemy em Pydantic
