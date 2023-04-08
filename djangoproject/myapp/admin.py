# Este archivo nos permitira añadir modelos a la interfaz de administración de Django o (Aplicaciiones)
# También podremos agregar modelos a la interfaz de administración de Django

# Importamos la librería admin de Django para poder registrar los modelos
from django.contrib import admin

# Importamos los modelos que hemos creado en el archivo models.py
from .models import Proyecto, task


# Register your models here.
# Ahora agregaremos los modelos a la interfaz de administración de Django
# Agregamos el modelo Proyecto a la interfaz de administración de Django
admin.site.register(Proyecto)


# Creamos una clase para personalizar la interfaz de administración de Django
class taskAdmin(admin.ModelAdmin):

    # Definimos la fecha de creación como campo de solo lectura tanto en la interfaz de administración de Django como en la base de datos
    readonly_fields = ('created',)


# Agregamos el modelo task a la interfaz de administración de Django
admin.site.register(task, taskAdmin)

# Agregamos el modelo User a la interfaz de administración de Django
# admin.site.register(User)
