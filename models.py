from sqlalchemy import create_engine, Column, Integer, String, Boolean, Enum, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from enum import Enum
# Criar conexão com o banco de dados SQLite
db = create_engine('sqlite:///banco-api.db')

# Criar a classe base para os modelos
Base = declarative_base()

# Criar as classes/tables do banco de dados
# Usuario, Pedido, ItensPedido   
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=False, unique=True)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean)
    
class Pedido(Base):
    __tablename__ = 'pedidos'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    usuario_id = Column("usuario_id", Integer, ForeignKey('usuarios.id'))
    valor_total = Column("valor_total", Float)

class ItensPedido(Base):
    __tablename__ = 'itens_pedido'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    pedido_id = Column("pedido_id", Integer, ForeignKey('pedidos.id'))
    produto = Column("produto", String)
    quantidade = Column("quantidade", Integer)
    preco_unitario = Column("preco_unitario", Float)
# Executar a criação dos metadados no banco de dados