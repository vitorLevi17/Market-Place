import os
import requests
from django.shortcuts import render
from dotenv import load_dotenv
load_dotenv()
def produto(request,produto):
    url = 'http://127.0.0.1:5000/Produto/'+str(produto)
    token = os.getenv('TOKEN')
    headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers).json()
    return render(request,'produtos/produto.html',{'context':response})
def categorias(request,categoria):
    url = 'http://127.0.0.1:5000/ProdutoCategoria/'+str(categoria)
    token = os.getenv('TOKEN')
    headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url,headers=headers).json()
    return render(request,'produtos/categorias.html',{'context':response})
# def preco_produto(request,preco_min,preco_max):
#     url = 'http://localhost:5000/Produto/'+str(preco_min)+'/'+str(preco_max)+'/'
#     token = os.getenv('TOKEN')
#     headers = {
#         'Authorization': f'Token {token}',
#         'Content-Type': 'application/json'
#     }
#     response = requests.get(url, headers=headers).json()
#     return render(request, 'sistema/index.html', {'context': response})