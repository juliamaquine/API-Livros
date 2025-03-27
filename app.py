from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/")
def init_presentation():
    return jsonify ({"mensagem":"Seja bem-vindo ao sistema de doação de livros!"})

def init_db():
    with sqlite3.connect("database.db") as conn:
        conn.execute("""
                    CREATE TABLE IF NOT EXISTS LIVROS(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     titulo TEXT NOT NULL,
                     categoria TEXT NOT NULL,
                     autor TEXT NOT NULL,
                     imagem_url TEXT NOT NULL
                     );
                     """)
        
init_db()

@app.route("/doar", methods = ["POST"])
def doar():

    dados = request.get_json()
    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    imagem_url = dados.get("imagem_url")

    with sqlite3.connect("database.db") as conn:
        conn.execute(f"""
                    INSERT INTO LIVROS(titulo, categoria, autor, imagem_url)
                    VALUES ('{titulo}','{categoria}','{autor}','{imagem_url}')
                     """)
    return jsonify({"mensagem":"Livro doado com sucesso!"}), 201

if __name__ == "__main__": 
    app.run()