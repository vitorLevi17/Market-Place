from decimal import Decimal

from dotenv import load_dotenv
import os
import requests
load_dotenv()

# def reduzirEstoque(produto ,preco, quantidade):
#     url = 'http://127.0.0.1:5000/Produto/' + str(produto)
#     token = os.getenv('TOKEN')
#     body = {
#         "preco": preco,
#         "quantidade": quantidade
#     }
#     headers = {
#         'Authorization': f'Token {token}',
#         'Content-Type': 'application/json'
#     }
#     response = requests.get(url,headers).json()
#     print(response['quantidade'])
# reduzirEstoque(2,10,2)

def requisitarProduto(produto):
    url = 'http://127.0.0.1:5000/Produto/' + str(produto)
    token = os.getenv('TOKEN')
    headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers).json()
    return response
def requisitarProdutoCategoria(categoria):
    url = 'http://127.0.0.1:5000/ProdutoCategoria/' + str(categoria)
    token = os.getenv('TOKEN')
    headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers).json()
    return response
def requisitarFretes(cep):
    url = 'https://www.melhorenvio.com.br/api/v2/me/shipment/calculate/'
    token = os.getenv('TOKEN_MELHOR_ENVIO')
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'User-Agent': 'vitorl@gmail.com'
    }
    body = {
        "from": {
            "postal_code": "40050000"
        },
        "to": {
            "postal_code": cep
    },
        "package": {
            "height": 4,
            "width": 12,
            "length": 17,
            "weight": 0.3
    }
    }
    response = requests.post(url,headers=headers,json=body)
    return response.json()

def requisitarFreteId(cep,id):
    url = 'https://www.melhorenvio.com.br/api/v2/me/shipment/calculate/'+str(id)
    token = os.getenv('TOKEN_MELHOR_ENVIO')
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'User-Agent': 'vitorl@gmail.com'
    }
    body = {
        "from": {
            "postal_code": "40050000"
        },
        "to": {
            "postal_code": cep
    },
        "package": {
            "height": 4,
            "width": 12,
            "length": 17,
            "weight": 0.3
    }
    }
    response = requests.post(url,headers=headers,json=body)
    result = response.json()
    preco = Decimal(result.get('price'))
    return preco
