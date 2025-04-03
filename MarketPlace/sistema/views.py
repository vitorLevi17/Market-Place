import os
from django.contrib.auth.models import User
from django.contrib import auth,messages
from django.shortcuts import render,redirect
import requests
from .forms import LoginForm
from dotenv import load_dotenv

load_dotenv()
def index(request):
    url = 'http://127.0.0.1:5000/Produto/'
    resposta = requests.get(url)
    resposta_json = resposta.json()
    #'http://127.0.0.1:8000/Produto/?search=Book 2'
    return render(request,'index.html',{'context':resposta_json})
def teste(request):
    url = 'http://127.0.0.1:5000/Produto/10/'
    token = os.getenv('TOKEN')

    resposta = requests.get(url)

    data = resposta.json()
    preco = data.get('preco',0)
    quantidade = data.get('quantidade',0)
    quantidade_vendida = 3
    nova_quantidade = quantidade-quantidade_vendida
    request_patch = {
        'preco': preco,
        'quantidade': nova_quantidade
    }
    headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json'
    }
    resposta = requests.patch(url,json=request_patch,headers=headers)
    if resposta.status_code == 200:
        print("Tudo certo na Bahia")

    return render(request,'teste.html',{'resposta':resposta.json()})
def entrar(request):
    login = LoginForm()

    if request.method == 'POST':
        login = LoginForm(request.POST)
        if login.is_valid():
            email_login = login.cleaned_data["email"]
            senha_login = login.cleaned_data["senha"]

            if(User.objects.filter(email = email_login)):
                usuario_credencias = User.objects.get(email=email_login)
                user = auth.authenticate(
                    request,
                    username = usuario_credencias.username,
                    password = senha_login
                )
                if user != None:
                    auth.login(request,user)
                    return redirect('index')
                else:
                    messages.error(request,"Usuario ou senha incorretos")
                    return redirect('entrar')
            else:
                messages.error(request,"Email não encontrado")
        else:
            messages.error(request,"Email invalido")
    return render(request,'entrar.html',{'login':login})