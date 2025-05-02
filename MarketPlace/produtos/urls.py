from django.urls import path
from .views import categorias,produto#,preco_produto

urlpatterns = [
    path('categorias/<int:categoria>/', categorias, name='categorias'),
    path('produto_view/<int:produto>/',produto,name='produto')#,
    #path('preco_produto/<str:preco_min>/<str:preco_max>/',preco_produto,name='preco_produto')
]
