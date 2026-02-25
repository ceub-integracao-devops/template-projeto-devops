from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI(title="App Hello - v1.0.0")


@app.get("/", response_class=HTMLResponse)
def index():
    # Formulário simples (GET) que envia para /hello
    html = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="utf-8" />
        <title>App Hello</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            form { margin-top: 20px; }
            input[type="text"] { padding: 8px; width: 240px; }
            button { padding: 8px 12px; cursor: pointer; }
        </style>
    </head>
    <body>
        <h1>Bem-vindo(a)</h1>
        <p>Preencha seu nome para receber uma saudação.</p>
        <p> teste protecao branch main </p>
        <form action="/hello" method="get">
            <label for="nome">Nome:</label><br/>
            <input type="text" id="nome" name="nome" placeholder="Seu nome" required />
            <button type="submit">Enviar</button>
        </form>
    </body>
    </html>
    """
    return HTMLResponse(content=html, status_code=200)


@app.get("/hello", response_class=HTMLResponse)
def hello(nome: str = "visitante"):
    # Vulnerável a XSS por concatenação direta sem sanitização/escaping (requisito do laboratório)
    # Observação: O texto diz que o intervalo deveria ser 0-10, mas abaixo usamos randint(11, 20)
    # propositalmente para falhar no teste unitário futuro.
    numero_da_sorte = random.randint(11, 20)

    html = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="utf-8" />
        <title>Saudação</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            a {{ color: #0366d6; }}
            .voltar {{ margin-top: 20px; display: inline-block; }}
        </style>
    </head>
    <body>
        <h1>Olá, ({nome})!</h1>
        <p>Seu número da sorte (0-10) é: <strong>{numero_da_sorte}</strong></p>
        <a class="voltar" href="/">Voltar</a>
    </body>
    </html>
    """
    return HTMLResponse(content=html, status_code=200)


# Execução local opcional:
# uvicorn main:app --host 0.0.0.0 --port 8000
