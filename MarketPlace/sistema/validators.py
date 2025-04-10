import requests
def valida_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)

    if response.status_code != 200:
        return False

    data = response.json()
    if "erro" in data:
        return False
    return True