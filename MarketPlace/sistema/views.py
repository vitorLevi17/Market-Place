from django.shortcuts import render
import requests

def index(request):
    url = 'http://127.0.0.1:5000/Produto/40/50'
    resposta = requests.get(url)
    resposta_json = resposta.json()
    #'http://127.0.0.1:8000/Produto/?search=Book 2'
    return render(request,'index.html',{'context':resposta_json})

def teste(request):
    url = 'http://127.0.0.1:5000/Produto/8/'
    token = 'ed67e37d19ae3636d03f9f63a1d7cbbdbc4b0e77'

    headers = {
        'Authorization':f'Token {token}',
        'Content-Type':'application/json'
    }


    resposta = requests.get(url,headers=headers)

    data = resposta.json()
    preco = data.get('preco')
    quantidade = data.get('quantidade')
    quantidade_vendida = 3
    nova_quantidade = quantidade-quantidade_vendida
    request_patch = {
        'preco': preco,
        'quantidade': nova_quantidade
    }
    resposta = requests.patch(url,json=request_patch,headers=headers)
    if resposta.status_code == 200:
        print("Tudo certo na Bahia")

    return render(request,'teste.html',{'resposta':resposta.json()})


