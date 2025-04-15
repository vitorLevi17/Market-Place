from django.urls import path
from .views import index, teste,entrar,cadastro ,logout, receber_email,mudar_senha

urlpatterns = [
    path('',index,name='index'),
    path('teste/',teste,name='teste'),
    path('entrar/',entrar,name='entrar'),
    path('cadastro/',cadastro,name='cadastro'),
    path('logout/',logout,name='logout'),
    path('rec_senha/',receber_email,name='rec_senha'),
    path('mudar_senha/<int:id>/',mudar_senha,name='mudar_senha')
]