# Este archivo nos permitira añadir modelos a la interfaz de administración de Django o (Aplicaciiones)
# También podremos agregar modelos a la interfaz de administración de Django


from django.contrib import admin
# Importamos los modelos que hemos creado en el archivo models.py
from .models import Proyecto, task

# Register your models here.

# Ahora agregaremos los modelos a la interfaz de administración de Django
admin.site.register(Proyecto)
admin.site.register(task)
