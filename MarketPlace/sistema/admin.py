from django.contrib import admin
from .models import Usuarios

class listaUsuario(admin.ModelAdmin):
    # list_display = ("usuario", "nm_doador", "cpf", "cep")
    # list_display_links = ("usuario", "nm_doador")
    # search_fields = ("nm_doador",)
    list_per_page = 10


# Register your models here.
admin.site.register(Usuarios,listaUsuario)
