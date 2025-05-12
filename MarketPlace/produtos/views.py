import os
import requests
from django.shortcuts import render,redirect
from dotenv import load_dotenv
from sistema.models import Favoritos
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Compra
from sistema.validators import valida_cep
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
    url = 'http://127.0.0.1:5000/Produto/' + str(produto)
    token = os.getenv('TOKEN')
    headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers).json()
    usuario = request.user
    produto = produto

    if not Favoritos.objects.filter(usuario=usuario,produto=produto).exists():
        favoritos = Favoritos.objects.create(usuario = usuario,produto = produto)
        favoritos.save()
        messages.success(request,"Item favoritado com sucesso")
    else:
        messages.error(request,"Produto já salvo")
    return render(request,"produtos/produto.html",{'context':response})
@login_required(login_url='/entrar/')
def lista_favoritos(request):
    usuario = request.user
    favoritos = Favoritos.objects.filter(usuario=usuario)
    lista_favoritos = []
    for favorito in favoritos:
        url = 'http://127.0.0.1:5000/Produto/' + str(favorito.produto)
        token = os.getenv('TOKEN')
        headers = {
            'Authorization': f'Token {token}',
            'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers).json()
        lista_favoritos.append(response)

    return render(request, 'produtos/lista_favoritos.html', {'context': lista_favoritos})
@login_required(login_url='/entrar/')
def desfavoritar(request,produto):
    url = 'http://127.0.0.1:5000/Produto/' + str(produto)
    token = os.getenv('TOKEN')
    headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers).json()
    usuario = request.user
    favoritos = Favoritos.objects.get(usuario=usuario,produto=produto)
    favoritos.delete()
    messages.success(request,"Item excluido com sucesso")
    return render(request,"produtos/produto.html",{'context':response})

def compra(request,produto):
    url = 'http://127.0.0.1:5000/Produto/' + str(produto)
    token = os.getenv('TOKEN')
    headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers).json()
    form = Compra(request.POST)
    quantidade = form['quantidade'].value()
    cep = form['cep'].value()
    if not form.is_valid():
        messages.error(request,'A quantidade deve ser maior ou igual a 1')
    elif valida_cep(cep) != True:
        messages.error(request, 'CEP inválido')
    else:
        messages.success(request,'tudo certo')
        #1/2/12 frete

    return render(request,"produtos/compra.html",{'context':response,'form':form})

# def preco_produto(request,preco_min,preco_max):
#     url = 'http://localhost:5000/Produto/'+str(preco_min)+'/'+str(preco_max)+'/'
#     token = os.getenv('TOKEN')
#     headers = {
#         'Authorization': f'Token {token}',
#         'Content-Type': 'application/json'
#     }
#     response = requests.get(url, headers=headers).json()
#     return render(request, 'sistema/index.html', {'context': response})