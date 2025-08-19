from django.urls import path
from .views import *

urlpatterns = [
    path('categorias/<int:categoria>/', categorias, name='categorias'),
    path('produto_view/<int:produto>/',produto,name='produto'),
    path('favoritos/<int:produto>/',favoritos,name='favoritos'),
    path('lista_favoritos/',lista_favoritos,name='lista_favoritos'),
    path('desfavoritar/<int:produto>/',desfavoritar,name='desfavoritar'),
    path('calcula_total/<int:produto>/',calcula_total,name='calcula_total'),
    path('fim_compra/',pos_pagamento,name='pos_pagamento'),
    path('compras/',compras,name='compras')
    #path('preco_produto/<str:preco_min>/<str:preco_max>/',preco_produto,name='preco_produto')
]
