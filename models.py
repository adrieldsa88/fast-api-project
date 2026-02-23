from sqlalchemy import create_engine, Column, Integer, String, Boolean, Enum, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType
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
    admin = Column("admin", Boolean, default=False)
    
    def __init__(self, nome: str, email: str, senha: str, ativo: bool = True, admin: bool = False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin
    
class Pedido(Base):
    __tablename__ = 'pedidos'
    
    STATUS_PEDIDO = (
        ("PENDENTE", "PENDENTE"),
        ("CONCLUIDO", "CONCLUIDO"), 
        ("CANCELADO", "CANCELADO")
        )
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", ChoiceType(STATUS_PEDIDO)) 
    usuario_id = Column("usuario_id", Integer, ForeignKey('usuarios.id'))
    valor_total = Column("valor_total", Float)
    
    def __init__(self, usuario_id: int, status: str = "pendente", valor_total: float = 0.0):
        self.usuario_id = usuario_id
        self.status = status
        self.valor_total = valor_total

class ItensPedido(Base):
    __tablename__ = 'itens_pedido'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    pedido_id = Column("pedido_id", Integer, ForeignKey('pedidos.id'))
    produto = Column("produto", String)
    quantidade = Column("quantidade", Integer)
    preco = Column("preco", Float)
    
    def __init__(self, pedido_id: int, produto: str, quantidade: int, preco_unitario: float):
        self.pedido_id = pedido_id
        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        
# Executar a criação dos metadados no banco de dados