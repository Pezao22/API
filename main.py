from fastapi import FastAPI

from pydantic import BaseModel

import database.db_cfg as db

app = FastAPI()

class add(BaseModel):
    nome : str
    email: str
    telefone: str

class rem(BaseModel):
    coluna: str
    valor: str

class up(BaseModel):
    coluna: str
    novo_valor: str
    atual_valor: str

# Pagina inicial com breve explicação de uso
@app.get("/")
def page_inicial():
    tx = 'BEM VINDO A API DO PEZAO\nEsta é uma mini API que faz alterações diretamente em um bando de cados configurado pelo usuario\n o sistema ainda esta em desenvolvimento é pode conter bugs\n\n O link abaixo te encaminha para a documentação de utilização\n  Link: www.localhost:8000/get/   '
    return {"Descrição de uso": tx}

# OBTER BANCO DE DADOS
@app.get("/get")
def ler_dados():
    dados = db.select()
    return {"database": dados}

# ADICIONAR INFORMAÇOES AO BANCO DE DADOS
@app.post("/add/")
async def adicionar_db(add: add):
    db.add(add.nome,add.email,add.telefone)
    return add

# REMOVER INFORMAÇOES DO BANCO DE DADOS
@app.post("/rem/") #db.rem(colun,valor)
async def remove_db(rem: rem):
    db.rem(rem.coluna,rem.valor)
    return rem

# ATUALIZAR ALGUMA INFORMAÇAO EXISTENTE NO BANCO DE DADOS
@app.post("/update/")
async def update_db(up: up):
    db.update(up.coluna,up.novo_valor,up.atual_valor)
    return up

'''
INICIAR API

uvicorn main:app --reload  {ONDE ESTA MAIN:APP SERIA NOME_APP:APP}

LINK DA DOCUMENTAÇÃO DA API http://127.0.0.1:8000/docs

ADICIONAR DADOS

{
  "nome": "string", -- nome que deseja adicionar
  "email": "string", -- email que deseja adicioncar
  "telefone": "string" -- telefone que deseja adicionar
}

REMOVER DADOS

{
  "coluna": "string", -- nome da coluna que vamos encontrar o valor a ser removido
  "valor": "string" -- qual valor devemos procurar para remover a linha da database
}

ATUALIZAR DADOS

{
  "coluna": "string", -- nome da coluna que vamos encontrar o valor a ser alterado
  "novo_valor": "string", -- qual é o novo valor a ser adicionado
  "atual_valor": "string"  -- qual é o valor atual que voce seja substituir
}

Exemplo de utilização usando requests [python]

import requests

link = 'http://localhost:8000/add/'

data ={
  'nome': 'cliche',
  'email': 'sla@gmail.com',
  'telefone': '123321123'
}

requisicao = requests.post(link,json = data)


'''