from django.urls import path
from .views import categorias,produto,favoritos#,preco_produto

urlpatterns = [
    path('categorias/<int:categoria>/', categorias, name='categorias'),
    path('produto_view/<int:produto>/',produto,name='produto'),
    path('favoritos/<int:produto>/',favoritos,name='favoritos')
    #path('preco_produto/<str:preco_min>/<str:preco_max>/',preco_produto,name='preco_produto')
]
