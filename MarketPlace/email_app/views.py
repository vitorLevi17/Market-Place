from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

def envia_email(request):
    send_mail('Assunto','Essa é a msg','vitorlevimenezessantos17@gmail.com',['vitorlevimenezessantos@outlook.com'])
    return HttpResponse("Olá")
