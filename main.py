from fastapi import FastAPI

app = FastAPI(
    title="AgendamentoMensagensWhatsapp",
    description="API que fornece os métodos para criação e agendamento de mensagens para o Whatsapp",
    version="1.0.0"
)

from agendamento_mensagem_whatsapp.src.routes.auth_routes import auth_router
from agendamento_mensagem_whatsapp.src.routes.mensage_routes import mensage_router

app.include_router(auth_router)
app.include_router(mensage_router)


#Para executar rode uvicorn main:app --reload