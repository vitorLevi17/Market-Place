import os
from django.contrib.auth.models import User
from django.contrib import auth,messages
from django.shortcuts import render,redirect
import requests
from .forms import LoginForm,UsuarioForm,ReceberEmailForm,MudarSenhaForm
from dotenv import load_dotenv
from validate_docbr import CPF
from .validators import valida_cep
import re
from .models import Usuarios
load_dotenv()
def index(request):
    url = 'http://127.0.0.1:5000/Produto/'
    token = os.getenv('TOKEN')
    headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json'
    }
    resposta = requests.get(url,headers=headers)
    resposta_json = resposta.json()
    #'http://127.0.0.1:8000/Produto/?search=Book 2'
    return render(request,'index.html',{'context':resposta_json})
def teste(request):
    url = 'http://127.0.0.1:5000/Produto/15/'
    token = os.getenv('TOKEN')
    headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json'
    }

    resposta = requests.get(url,headers=headers)

    data = resposta.json()
    preco = data.get('preco',0)
    quantidade = data.get('quantidade',0)
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

def cadastro(request):
    form = UsuarioForm()
    cpfvalidador = CPF()

    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        username = form["username"].value() #
        nome = form["nome"].value()#
        sobrenome = form["sobrenome"].value()#
        email = form["email"].value()
        senha = form["senha"].value()
        senha1 = form["senha1"].value()
        cpf = form["cpf"].value()
        cep = form["cep"].value()
        complemento = form["complemento"].value()#
        telefone = form["telefone"].value()

        #validações
        if senha1 != senha:
            messages.error(request, "As senhas não coincidem ")
            return redirect('cadastro')

        if cpfvalidador.validate(cpf) == False or Usuarios.objects.filter(cpf=cpf).exists():
            messages.error(request, "CPF inválido ")
            return redirect('cadastro')

        if not valida_cep(cep):
            messages.error(request, "CEP inválido")
            return redirect('cadastro')

        if not re.fullmatch(r"^\d{11}$", telefone) or Usuarios.objects.filter(telefone=telefone).exists():
            messages.error(request, "Número de telefone inválido")
            return redirect('cadastro')

        if form.is_valid() and not User.objects.filter(email=email).exists():
            usuario = User.objects.create_user(
                username=username,
                first_name = nome,
                last_name = sobrenome,
                email=email,
                password=senha1
            )
            usuario.save()
            resto_usuario = Usuarios.objects.create(
                usuario = usuario,
                cpf = cpf,
                telefone = telefone,
                cep = cep,
                complemento = complemento
            )
            resto_usuario.save()
            return redirect('index')
        else:
            messages.error(request, "Email inválido ")
            return redirect('cadastro')

    return render(request,'cadastro.html',{'form':form})

def logout(request):
    auth.logout(request)
    messages.success(request,"Logout feito")
    return redirect('entrar')

def receber_email(request):
    form = ReceberEmailForm(request.POST)
    email = form['email'].value()
    if form.is_valid() and User.objects.filter(email=email).exists():
        usuario = User.objects.get(email=email)
        id_usuario = usuario.id
        print(id_usuario,email)
        # enviar email para usuario
        # Passar endereço de email no parametro para metodo de envio de email
        messages.success(request,'Tudo certo')
        return redirect('index')
    else:
        messages.success(request, 'Tudo errado')
    return render(request,'rec_senha.html',{'form':form})

def mudar_senha(request,id):
    form = MudarSenhaForm(request.POST)
    senha = form['senha'].value()
    senha1 = form['senha1'].value()

    if form.is_valid() and senha1 == senha:
        usuario = User.objects.get(id=id)

        usuario.set_password(senha1)
        usuario.save()
        messages.success(request, "Senha alterada com sucesso!")
        return redirect('index')
    else:
        messages.error(request,"Senhas não coincidem ou invalidas")

    return render(request,'mudar_senha.html',{'form':form,'id': id})