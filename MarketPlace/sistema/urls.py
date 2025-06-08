from django.urls import path
from .views import index,entrar,cadastro ,logout, receber_email,mudar_senha

urlpatterns = [
    path('',index,name='index'),
    path('entrar/',entrar,name='entrar'),
    path('cadastro/',cadastro,name='cadastro'),
    path('logout/',logout,name='logout'),
    path('receber_email/',receber_email,name='receber_email'),
    path('mudar_senha/<int:id>/',mudar_senha,name='mudar_senha')
]