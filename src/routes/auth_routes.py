from fastapi import APIRouter
from fastapi import Query

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def ususarios(teste:str = Query(description="Uma descrição do que é esse parametro")):
    """
    Lista todos os usuários
    """
    return {"mensagem": "Você vai listar todos os usuários"}