from django.db import models
from django.contrib.auth.models import User

class Usuarios(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11,null=False,blank=False,unique=True)
    telefone = models.CharField(max_length=13, null=False, blank=False, unique=True)
    cep = models.CharField(max_length=9, null=False, blank=False)
    #historico_doacoes = models.IntegerField(default=0)
    complemento = models.CharField(max_length=255, null=False, blank=False)
def __str__(self):
    return self.usuario


