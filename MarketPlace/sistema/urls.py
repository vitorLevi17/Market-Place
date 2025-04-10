from django.urls import path
from .views import index, teste,entrar,cadastro

urlpatterns = [
    path('',index,name='index'),
    path('teste/',teste,name='teste'),
    path('entrar/',entrar,name='entrar'),
    path('cadastro/',cadastro,name='cadastro'),
]