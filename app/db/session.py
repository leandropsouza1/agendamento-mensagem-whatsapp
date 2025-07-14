from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Criação da engine usando a URL do banco de dados
# engine = create_engine(
#    settings.DATABASE_URL,
#    connect_args={"check_same_thread": False} if settings.DATABASE_URL.startswith("sqlite") else {}
# )

connect_args = {}
if settings.DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}
else:
    connect_args = {}

engine = create_engine(settings.DATABASE_URL, connect_args=connect_args)

# Criação da classe base para os modelos
Base = declarative_base()

# Criação da fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Função para obter a sessão do banco (usada como dependência no FastAPI)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
