from django.urls import path
from .views import envia_email

urlpatterns = [
    path('',envia_email,name='envia_email'),
]