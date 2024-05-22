# Projeto FastAPI

Este projeto é uma aplicação simples de API REST construída com o framework FastAPI. Ele permite a criação, leitura, atualização e exclusão (CRUD) de usuários e tarefas.

## Funcionalidades

### Criação de usuários
`POST /users/`

### Criação de tarefas
`POST /tasks/`

### Leitura de tarefas
`GET /tasks/`

### Leitura de tarefa por ID
`GET /tasks/{task_id}`

### Atualização de tarefa
`PUT /tasks/{task_id}`

### Exclusão de tarefa
`DELETE /tasks/{task_id}`

## Documentação da API

A documentação completa da API, incluindo os modelos de dados e os parâmetros de cada endpoint, pode ser encontrada no Swagger UI. Para acessá-lo, inicie o servidor e visite o seguinte URL:

[http://localhost:8000/docs](http://localhost:8000/docs)

## Como executar o projeto

1. Instale as dependências do projeto com o comando `pip install -r requirements.txt`.
2. Inicie o servidor com o comando `uvicorn main:app --reload`.

Agora você pode fazer requisições para a API no endereço `http://localhost:8000`.
