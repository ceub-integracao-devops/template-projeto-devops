from main import app
from fastapi.testclient import TestClient
import re

client = TestClient(app)

def test_hello_lucky_number_range():
    """
    Testa se o número da sorte exibido no HTML do endpoint /hello
    está dentro do intervalo esperado (0 a 10).
    """
    # 1. Faz a requisição simulando o usuário
    response = client.get("/hello?nome=Professor")
    
    assert response.status_code == 200
    
    # 2. Extrai o conteúdo HTML
    html_content = response.text
    
    # 3. Usa Expressão Regular para encontrar o número entre as tags <strong>
    # Buscamos o padrão: <strong>(um ou mais dígitos)</strong>
    match = re.search(r"<strong>(\d+)</strong>", html_content)
    
    assert match is not None, "Não foi possível encontrar o número da sorte no HTML"
    
    numero_extraido = int(match.group(1))
    
    # 4. A Validação Real (Onde o código atual vai falhar)
    # O requisito diz 0-10, mas o código entrega 11-20.
    print(f"\nNúmero extraído do HTML: {numero_extraido}")
    assert 0 <= numero_extraido <= 10, f"Erro: O número {numero_extraido} está fora do intervalo 0-10!"

