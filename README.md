# API de Usuários com Django e PostgreSQL

Este projeto foi desenvolvido como parte de um **teste técnico** para uma vaga de desenvolvedor backend. Ele implementa uma API RESTful utilizando **Django** e **Django REST Framework**, com autenticação por **JWT** e manipulação de HTML armazenado no banco de dados **PostgreSQL**

## 📜 Pré-requisitos
Certifique-se de ter uma das ferramentas abaixo instaladas.
* **Docker**
<br>OU 
* **Python 3**

## 🚀 Iniciar a aplicação 
Primeiramente, você deve clonar esse repositório para sua máquina.
```bash
git clone https://github.com/gustaoliveira1/django-rest-api
```


### 🐋 Docker
A aplicação foi conteinerizada com docker, logo, caso tenha docker instalada em sua máquina basta utilizar o seguinte comando:
```bash
docker compose up -d --build
```

### 🖖 Manualmente
Caso não tenha docker instalado em sua máquina, é possivel iniciar a aplicação seguindo alguns simples passos.

1. Crie um arquivo `.env`, com todos os campos necessários para que a aplicação consiga acessar o banco de dados, como em `.env.example`.
2. Crie um ambiente virtual e o ative.
```bash
# Criação do embiente virtual
python -m venv .venv

# Ativação no linux
source .venv/bin/activate
# Ativação no Windows 
.venv/Scripts/activate
```
3. Instale todos os packages necessários para que o projeto seja iniciado.
```bash
python -m pip install -r requirements.txt
```
4. Rode as migrations para configurar o banco de dados.
```bash
python manage.py migrate
```
5. Finalmente, inicie a aplicação.
```bash
python manage.py runserver
```

Em ambas as abordagens o projeto ficara disponível a partir do endereço http://127.0.0.1:8000

## 📋 Funcionalidades

### CRUD de Usuário

* POST /usuarios/ – Criar um novo usuário.
* POST /usuarios/auth/ – Gera um token de autorição.
* GET /usuarios/{id}/ – Obter os detalhes de um usuário específico.
* PUT /usuarios/{id}/ – Atualizar um usuário.
* DELETE /usuarios/{id}/ – Remover um usuário.

### Manipulação de HTML Armazenado
* POST /licoes/ – Cria uma nova lição.
* POST /licoes/{id}/ – Retorna as informações da lição.
* POST /licoes/{id}/editar-html/ – Modifica o conteúdo HTML diretamente no banco.

Para mais informações de como utilizar as rotas veja o conteúdo da pasta `doc`.