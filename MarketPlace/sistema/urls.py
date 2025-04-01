from django.urls import path, include
from .views import index, teste,entrar

urlpatterns = [
    path('',index,name='index'),
    path('teste/',teste,name='teste'),
    path('entrar/',entrar,name='entrar'),
    path('email/',include('email_app.urls'))
]