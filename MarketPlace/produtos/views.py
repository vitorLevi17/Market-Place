import os
import requests
from django.shortcuts import render
from dotenv import load_dotenv
from sistema.models import Favoritos
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
@login_required(login_url='/entrar/')
def favoritos(request,produto):
    usuario = request.user
    produto = produto
    favoritos = Favoritos.objects.create(usuario = usuario,produto = produto)
    favoritos.save()
    messages.success(request,"Item registrado com sucesso")
    return render(request,"produtos/produto.html")

# @login_required(login_url='/entrar/')
# def lista_favoritos(request):
#     usuario = request.user


# def preco_produto(request,preco_min,preco_max):
#     url = 'http://localhost:5000/Produto/'+str(preco_min)+'/'+str(preco_max)+'/'
#     token = os.getenv('TOKEN')
#     headers = {
#         'Authorization': f'Token {token}',
#         'Content-Type': 'application/json'
#     }
#     response = requests.get(url, headers=headers).json()
#     return render(request, 'sistema/index.html', {'context': response})