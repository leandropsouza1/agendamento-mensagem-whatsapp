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
    pedido = Column("pedido", ForeignKey("pedido.id"))

    def __init(self, quantidade: int, sabor:str, tamanho:str, preco_unitario:Decimal, pedido:int):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido