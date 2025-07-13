# 📦 Estrutura Base de Projeto Python

Este repositório define uma **estrutura base modular e produtiva para projetos Python**, incluindo organização de código, testes, ambiente virtual e automações de desenvolvimento.

---

## 📁 Estrutura do Projeto

```bash
.
├── meu_projeto
│   ├── src                  # Código-fonte da aplicação
│   │   ├── app.py
│   │   └── main.py          # Ponto de entrada do projeto (executável com python -m)
│   └── test                 # Testes automatizados com pytest
│       └── test_nome.py
├── .env                     # Variáveis de ambiente (não deve ser versionado)
├── .gitignore               # Arquivos ignorados pelo Git
├── pyproject.toml           # Configuração principal do projeto: nome, versão, dependências e ferramentas
├── README.md                # Documentação do Projeto
└── uv.lock                  # Dependências com versões exatas, usado para reprodutibilidade com a ferramenta UV
```

##Para ver a Estrutura do Projeto

```bash
tree
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
