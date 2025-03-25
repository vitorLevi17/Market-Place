from django.urls import path
from .views import index, teste,testef

urlpatterns = [
    path('',index,name='index'),
    path('teste/',teste,name='teste'),
    path('testef/',testef,name='testef')
]