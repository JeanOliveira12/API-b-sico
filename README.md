# API de Usuários - Projeto QA

API desenvolvida com FastAPI para prática de testes manuais e automatizados.

## Tecnologias
- Python
- FastAPI
- Uvicorn
- Pytest (em breve)

## Como rodar

```bash
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn
python -m uvicorn app.main:app --reload

```md
## Endpoints

### Criar usuário
POST /usuarios

### Listar usuários
GET /usuarios

### Deletar usuário
DELETE /usuarios/{id}

## Exemplo

```json
{
  "nome": "Jean",
  "email": "jean@email.com"
}


```md
## Regras de negócio

- Email deve ser único
- ID é gerado automaticamente

## Testes

- Criação de usuário
- Validação de erro 422
- Teste de email duplicado
- Teste de deleção

## Objetivo

Projeto desenvolvido para prática de testes de API e entrada na área de QA.