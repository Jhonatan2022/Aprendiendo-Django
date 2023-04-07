# Este archivo nos permitira configurar esta aplicación, pero solo esta sección de la aplicación

from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
