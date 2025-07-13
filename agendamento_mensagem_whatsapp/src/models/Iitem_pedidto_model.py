from decimal import Decimal
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, DECIMAL
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

Base = declarative_base()

class ItemPedido(Base):
    __tablename__ = "itens_pedidos"

    id = Column("id", primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco_unitario", DECIMAL)
    pedido = 