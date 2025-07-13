# 📦 Estrutura Base de Projeto Python

Este repositório define uma **estrutura base modular e produtiva para projetos Python**, incluindo organização de código, testes, ambiente virtual e automações de desenvolvimento.

---

## 📁 Estrutura do Projeto

```bash

├── app/                          # Código-fonte da aplicação
│   ├── api/                      # Rotas da API agrupadas por versão ou domínio
│   │   └── v1/
│   │       ├── __init__.py
│   │       └── usuario.py        # Rotas relacionadas a usuários
│
│   ├── core/                     # Configurações e inicialização da aplicação
│   │   ├── __init__.py
│   │   ├── config.py             # Carrega variáveis do .env usando Pydantic
│   │   └── settings.py           # Instância de configurações globais
│
│   ├── db/                       # Acesso ao banco de dados e migrations
│   │   ├── __init__.py
│   │   ├── base.py               # Base declarativa + import dos modelos
│   │   ├── session.py            # Engine, SessionLocal e dependências
│   │   └── migrations/           # Arquivos de migração gerados pelo Alembic
│   │       ├── versions/         # Scripts de migração versionados
│   │       ├── env.py            # Configura o ambiente do Alembic
│   │       ├── script.py.mako    # Template dos scripts
│   │       └── alembic.ini       # (opcional) Arquivo de config Alembic
│
│   ├── models/                   # Modelos SQLAlchemy usados no banco
│   │   ├── __init__.py
│   │   └── usuario.py            # Modelo de usuário
│
│   ├── schemas/                  # Schemas Pydantic para validação de entrada/saída
│   │   ├── __init__.py
│   │   └── usuario.py            # Schema de usuário (input/output)
│
│   ├── services/                 # Lógica de negócio da aplicação
│   │   ├── __init__.py
│   │   └── usuario_service.py    # Regras para manipulação de usuários
│
│   ├── dependencies.py           # Dependências reutilizáveis para injeção
│   └── main.py                   # Entrypoint principal do FastAPI (app)
│
├── tests/                        # Testes unitários e de integração
│   ├── __init__.py
│   └── test_usuario.py           # Testes da funcionalidade de usuário
│
├── .env                          # Variáveis de ambiente sensíveis (não deve ser versionado)
├── .gitignore                    # Ignora arquivos/pastas do Git
├── README.md                     # Documentação do projeto
├── pyproject.toml                # Configuração do projeto e dependências (uv/poetry)
├── uv.lock                       # Lockfile das dependências instaladas
└── .vscode/                      # (opcional) Configurações locais do VS Code


```

## Para ver a Estrutura Atualizada do Projeto

```bash
tree
```

## 📦 Gerenciamento de Pacotes com [uv](https://github.com/astral-sh/uv)

Este repositório utiliza o `uv` como gerenciador de pacotes ultrarrápido para ambientes virtuais.

> **Pré-requisitos**: Python ≥ 3.8 e `uv` instalado globalmente

### 🔧 Como instalar o `uv`:

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

ou via `pipx`:

```bash
pipx install uv
```

## Ajuste a estrutura com o nome do seu projeto

- Renomeie a pasta `meu_projeto` com o nome real do seu projeto.

- No arquivo `pyproject.toml`, substitua todas as ocorrências de `meu_projeto` pelo nome do seu projeto.

---

## 🚀 Execução

### Crie o ambiente virtual:

```bash
uv venv .venv
```

### Ative o ambiente virtual:

```bash
source .venv/bin/activate
```

### Sincronize as Bibliotecas:

```bash
uv sync
```

## 🤖 Rodando o Projeto com [Taskipy](https://pypi.org/project/taskipy/1.0.0/)

### 🔍 Verificar o lint do código:

```bash
task lint
```

### 🔎 Validar a formatação do código:

```bash
task pre_format
```

### 🧼 Formatar automaticamente o código:

```bash
task format
```

### 🚀 Executar o projeto:

```bash
task run
```

### 🧪 Rodar os testes:

```bash
task test
```

## Gerenciando De Comentário No Código com [TODO Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree)

Os comentários em código podem (e devem) ser utilizado para destacar melhorias, correções, etc que precisa ser realizadas. Podem ser utilizadas as seguintes Tags para ajudar no enendimento dos comentários

```python
# TODO: Implementar autenticação JWT
# FIXME: Corrigir validação de email
# BUG: Corrigir erro ao salvar usuário
# NOTE: Essa parte será refatorada na próxima sprint
# HACK: Solução temporária para timeout
```
