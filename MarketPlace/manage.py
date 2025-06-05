"""Django's command-line utility for administrative tasks."""
import os
import sys

#-Tela de compra(confirmar endereço, if request.user == true mnter info de endereço)
#Retirar um botão em COMPRA.HTML
#4- pix
#filtros - nome - autor - preco
#3- usuarios(email, esqueceu a senha)
#2- carregar as imgs


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
