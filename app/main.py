from fastapi import FastAPI

app = FastAPI(
    title="Agendamento de Mensagens",
    description="API que fornece os métodos para criação e agendamento de mensagens para o Whatsapp",
    version="1.0.0"
)

from app.api.v1.usuario_route import usuario_router
app.include_router(usuario_router)