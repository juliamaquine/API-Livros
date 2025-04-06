### API livros doados

essa é uma API feita com flask e SQlite para fins de estudos com o intuito de permitir cadastrar e listar os livros doados.

# Como rodar o projeto?

1. Faça o clone do repositório:

```bash
git clone <link do repositório>
cd nome_do_projeto
```

2. Criar um ambiente virtual

**Windows**

```bash
python -m venv venv 
source venv/Script/activate
```

**Linux/Mac**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:

```bash 
pip install -r requirements.txt
```

4. Reinicie o servidor:

```bash
python app.py 
```

A API estará disponível em  http://177.0.0.1:500/

# Endpoints

### POST /doar

Endpoint para cadastro das informações do livro doado.

**Envio das informações (JSON):**


```json

{
"titulo": "O Diario de Anne Frank",
"categoria": "Biografia",
"autor": "Anne Frank",
"imagem_url": "https://imagem.com"
}
```

**Resposta (201)**

```json
{
    "mensagem": "Livro doado com sucesso!"
}
```

### GET / retornar livros cadastrados

Retorna todos os livros cadastrados 

**Resposta(200):**

```json
{
"id": "0",
"titulo": "Diario de Anne Frank",
"categoria": "Biogradia",
"Autor": "Anne Frank",
"imagem_url": "https://exemplo.com"
}

```

### Tecnologias Utilizadas

- Python 3
- Flask
- SQLite
- Flask-CORS


```(colar

```
