from django.urls import path, include
from .views import index, teste,testef

urlpatterns = [
    path('',index,name='index'),
    path('teste/',teste,name='teste'),
    path('testef/',testef,name='testef'),
    path('email/',include('email_app.urls'))
]