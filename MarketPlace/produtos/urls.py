from django.urls import path
from .views import categorias

urlpatterns = [
    path('categorias/<int:categoria>/', categorias, name='categorias')
]
