from fastapi import APIRouter, Depends
from models import Usuario
from dependencies import get_session


# Define a rota de autenticação
auth_router = APIRouter(prefix="/auth", tags=["auth"])



@auth_router.post("/create_user")
async def create_user(nome: str,email: str, senha: str, session = Depends(get_session())):
    
    if session.query(Usuario).filter(Usuario.email == email).first():
        session.close()
        return {"mensagem": "Usuário já existe"}
    else:
        new_user = Usuario(nome,email,senha)
        session.add(new_user)
        session.commit()
        return {"mensagem": "Usuário criado com sucesso"}