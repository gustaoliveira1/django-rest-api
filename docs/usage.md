# 📚 Documentação
Esta documentação explica como utilizar cada rota da API, com exemplos em **curl** para facilitar o entendimento.
<hr>

## Usuários

### 1. Cria Usuário
Endpoint:
`POST /usuarios/`

**Exemplo de requisição**
```bash
curl -X POST http://127.0.0.1:8000/usuarios/ \
-H "Content-Type: application/json" \
-d '{
  "nome": "João Silva",
  "email": "joao@exemplo.com",
  "senha": "senha123",
  "data_de_nascimento": "1990-05-15"
}'
```
**Resposta**
```json
{
    "id":1,
    "nome":"João Silva",
    "email":"joao@exemplo.com",
    "data_de_nascimento":"1990-05-15"
}
```
### 2. Autenticação (Obter token JWT)
Endpoint:
`POST /usuarios/auth/`

**Exemplo de requisição**
```bash
curl -X POST http://127.0.0.1:8000/usuarios/auth/ \
-H "Content-Type: application/json" \
-d '{
  "email": "joao@exemplo.com",
  "password": "senha123"
}'
```
**Resposta**
```json
{
    "refresh": <REFRES_TOKEN>,
    "access": <ACCESS_TOKEN>
}                                                                                                                   
```
### 3. Obter usuário por ID
Endpoint:
`GET /usuarios/{id}/`

**Exemplo de requisição**
```bash
curl -X GET http://127.0.0.1:8000/usuarios/1/ \
-H "Authorization: Bearer <ACESS_TOKEN>"
```
**Resposta**
```json
{
  "id": 1,
  "nome": "João Silva",
  "email": "joao@exemplo.com",
  "data_de_nascimento": "1990-05-15"
}

```
### 4. Atualizar Usuário
Endpoint:
`PUT /usuarios/{id}/`

**Exemplo de requisição**
```bash
curl -X PUT http://localhost:8000/usuarios/1/ \
-H "Authorization: Bearer <ACESS_TOKEN>" \
-H "Content-Type: application/json" \
-d '{
  "nome": "João Silva Atualizado",
  "email": "joao@exemplo.com",
  "senha": "senha123",
  "data_de_nascimento": "1990-05-15"
}'
```
**Resposta**
```json
{
  "id": 1,
  "nome": "João Silva",
  "email": "joao@exemplo.com",
  "data_de_nascimento": "1990-05-15"
}
```
### 5. Deletar Usuário
Endpoint:
`DELETE /usuarios/{id}/`

**Exemplo de requisição**
```bash
curl -X DELETE http://localhost:8000/usuarios/1/ \
-H "Authorization: Bearer <ACESS_TOKEN>"

```
**Resposta**
```json
```
<hr>

## Lição

### 6. Criar lição
Endpoint:
`POST /licoes/`

**Exemplo de requisição**
```bash
curl -X POST http://localhost:8000/licoes/ \
-H "Authorization: Bearer <ACCESS_TOKEN>" \
-H "Content-Type: application/json" \
-d '{
  "titulo": "Hello world",
  "conteudo_html": "<h1>Hello world</h1>"
}'
```
**Resposta**
```json
{
  "id": 1,
  "titulo": "Hello world",
  "conteudo_html": "<h1>Hello world</h1>",
  "owner": 2
}
```

### 7. Modificar Conteúdo HTML da Lição
Endpoint:
`POST /licoes/`

**Exemplo de requisição**
```bash
curl -X POST http://localhost:8000/licoes/1/editar-html/ \
-H "Authorization: Bearer seu_token_jwt" \
-H "Content-Type: application/json" \
-d '{
  "conteudo_html": "<h1 style=\"color:red;\">Hello world!</h1>"
}'
```
**Resposta**
```json
{
  "id": 1,
  "titulo": "Hello world",
  "conteudo_html": "<h1>Hello world</h1>",
  "owner": 2
}
```