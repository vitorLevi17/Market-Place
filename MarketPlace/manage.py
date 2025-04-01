#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

#3- usuarios(criação,autenticação,email, zap e endereço de entrega)
#1- listar produtos (filtros)
#2- carregar as imgs
#4- api pix / cartão
#5- finalizar compra

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
