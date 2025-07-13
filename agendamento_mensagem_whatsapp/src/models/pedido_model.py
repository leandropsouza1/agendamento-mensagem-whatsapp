from decimal import Decimal
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, DECIMAL
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

Base = declarative_base()

class Pedido(Base):
    __tablename__ = "pedidos"

    STATUS_PEDIDO = (
        ("PENDENTE", "PENDENTE"),
        ("CANCELADO", "CANCELADO"),
        ("FINALIZADO", "FINALIZADO"),
    )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", ChoiceType(choices=STATUS_PEDIDO), default="PENDENTE")
    id_usuario = Column("id_usuario", ForeignKey("usuario.id"))
    preco = Column("preco", DECIMAL)

    def __init__(self, status:str, id_usuario:int, preco:Decimal):
        self.status = status
        self.id_usuario = id_usuario
        self.preco = preco
    