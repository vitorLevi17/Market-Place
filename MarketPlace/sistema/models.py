from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User

class Usuarios(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11,null=False,blank=False,unique=True)
    telefone = models.CharField(max_length=13, null=False, blank=False, unique=True)
    cep = models.CharField(max_length=9, null=False, blank=False)
    complemento = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return self.usuario

class FormaPag(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class Compra(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    forma_pag = models.ForeignKey(to=FormaPag,on_delete=models.CASCADE,related_name='forma_pag')
    produto = models.IntegerField(null=False,blank=False)
    data = models.DateTimeField(default=now)
    parcelas = models.IntegerField(default=1)
    quantidade = models.IntegerField(null=False,blank=False)
    frete_id = models.IntegerField(default=0)
    endereco = models.CharField(max_length=225,null=False)
    tempo_previsto = models.IntegerField(null=False,blank=False)
    tempo_chegada = models.IntegerField(null=True)
    valor_compra = models.FloatField(null=False,blank=False)
    status = models.IntegerField(default=1) #1-Não Entregue 2-Entregue

class Favoritos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.IntegerField(null=False, blank=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['usuario', 'produto'], name='unique_favorito')
        ]


