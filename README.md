# API

Api criado em Python utilizando FastApi, esta API permite ao usuario fazer alteraçoes diretamente no Banco de dados Utilidando os metodos POST e GET

Temos abaixo um breve tutotial de como usar

DEPENDENCIA

PYTHON,
FASTAPI,
BASEMODEL,
MYSQL.CONNECTOR

CONFIGURANDO MYSQL 

Preencha os campos alterando os dados de acordo com seu banco de dados

![image](https://user-images.githubusercontent.com/114784744/209484089-f8f2ecc4-79dd-4d3d-83b1-417b9c027305.png)


INICIAR API

uvicorn main:app --reload  {ONDE ESTA MAIN:APP SERIA NOME_APP:APP}

LINK DA DOCUMENTAÇÃO DA API http://127.0.0.1:8000/docs  

ADICIONAR DADOS [COM POST ]

{
  "nome": "string", -- nome que deseja adicionar
  "email": "string", -- email que deseja adicioncar
  "telefone": "string" -- telefone que deseja adicionar
}

REMOVER DADOS [COM POST ]

{
  "coluna": "string", -- nome da coluna que vamos encontrar o valor a ser removido
  "valor": "string" -- qual valor devemos procurar para remover a linha da database
}

ATUALIZAR DADOS [COM POST ]

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
