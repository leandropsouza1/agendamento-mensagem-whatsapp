from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.usuario_model import Usuario
from app.schemas.usuario_schema import UsuarioCreate

usuario_router = APIRouter(prefix="/usuarios", tags=["Usuários"])

#@usuario_router.post("/")
#def criar_usuario(usuario_schema:UsuarioCreate, db: Session = Depends(get_db)):
#    print("texto")

@usuario_router.get("/", response_model=list[dict])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return [{"id": u.id, "nome": u.nome, "email": u.email} for u in usuarios]
