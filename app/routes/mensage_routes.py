from fastapi import APIRouter
from fastapi import Query


mensage_router = APIRouter(prefix="/router", tags=["router"])

@mensage_router.get("/")
async def mensagem(teste:str = Query(description="Uma descrição do que é esse parametro")):
    """
    Lista de mensagens
    """
    return {"mensagem": "Você vai listar as mensagens"}