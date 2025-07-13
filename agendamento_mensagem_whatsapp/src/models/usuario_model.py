from decimal import Decimal

from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey, DECIMAL
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

#TODO Ver como consigo separ a criação do Engine
db = create_engine("sqlite:///agendamento_mensagem_whatsapp/db/agendamento-mensagem-whatapp.db")
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean, default=True)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome:str, email:str, senha:str, ativo:bool=True, admin:bool=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin



#TODO Criar um arquivo separado para classe Pedido
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


#TODO Criar um arquivo separado para classe ItemPedido
class ItemPedido(Base):
    id = Column("id", primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco_unitario", DECIMAL)
    pedido_id =  Column("id_pedido", ForeignKey("pedidos.id"))

    def __init__(self, quantidade:int, sabor:str, tamanho:int, preco_unitario:Decimal, pedido_id:int):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido_id = pedido_id
