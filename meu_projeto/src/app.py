import os

import dotenv
from openai import OpenAI

dotenv.load_dotenv()

client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
)

response = client.responses.create(
    model='gpt-4o',
    instructions='You are a coding assistant that talks like a pirate.',
    input='How do I check if a Python object is an instance of a class?',
)
print(response.output_text)


def Umafuncao(nome: str) -> str:
    return nome.capitalize()
