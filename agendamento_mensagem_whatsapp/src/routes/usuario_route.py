from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db.session import get_db
from src.models.usuario_model import Usuario

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@router.get("/", response_model=list[dict])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return [{"id": u.id, "nome": u.nome, "email": u.email} for u in usuarios]
