<h1 align="center">
    🔗 Todo-List API</a>
</h1>
<p align="center">🚀 API para  gerenciamento de usuários e de tarefas.</p>

<p align="center">
<img src="https://img.shields.io/badge/FastAPI-TODO_LIST_API-%2300fa?style=for-the-badge&logo=fastapi" alt="Badges"/>
</p>

### Status

<h4> 
	Fastapi To Do List 🚀 Finalizado
</h4>

### Features

- [x] Autenticação JWT
- [x] CRUD completo de usuário
- [x] CRUD completo de tarefas
- [x] Testes E2E
- [x] Middleware
- [x] Assincronismo
- [x] Tarefa de background
- [x] Inversão de controle por meio de injeção de dependência


### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina o Docker e o Docker compose e configurar o arquivo .env.production seguindo os nomes das variaveis que estam no .env.production.example

### 🎲 Rodando o Back End (servidor)

```bash
# Clone este branch
$ git clone --branch "enterpise-systems/fastapi-crud" git@github.com:Talismar/ifrn-ads.git "fastapi-crud"

# Acesse a pasta do fastapi-crud no terminal/cmd
$ cd fastapi-crud

# Execute a aplicação em modo de produção
$ docker compose build
$ docker compose up -d

# Caso queira executar os testes dentro do docker

# 1. Entre dentro do container
$ docker exec -i -t <container_name> /bin/bash 

# 2. instale duas dependencias
$ pip install pytest httpx

# 3. Execute os testes
$ pytest

# O servidor inciará na porta:8008 - acesse <http://localhost:8008/docs> 
```

### 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção da atividade:

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy-ORM](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [Pytest](https://docs.pytest.org/en)

### Autor
---

 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/92408845?v=4" width="100px;" alt=""/>
 <br />
 <sub><b>Talismar Fernandes Costa</b></sub>

---