from django.urls import path
from .views import categorias,produto,favoritos,lista_favoritos,desfavoritar#,preco_produto

urlpatterns = [
    path('categorias/<int:categoria>/', categorias, name='categorias'),
    path('produto_view/<int:produto>/',produto,name='produto'),
    path('favoritos/<int:produto>/',favoritos,name='favoritos'),
    path('lista_favoritos/',lista_favoritos,name='lista_favoritos'),
    path('desfavoritar/<int:produto>/',desfavoritar,name='desfavoritar')
    #path('preco_produto/<str:preco_min>/<str:preco_max>/',preco_produto,name='preco_produto')
]
