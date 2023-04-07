# Este archivo contiene los modelos de la aplicación en donde podremos crear clases que representen a las tablas de nuestra base de datos.

# Usaremos principlamente la clase models.py para proyectos y tareas
from django.db import models

# Importamos el modelo User para poder relacionar las tareas con los usuarios
from django.contrib.auth.models import User



# Create your models here.
class Proyecto(models.Model):
    # Definimos los campos de la tabla Proyecto y los tipos de datos que contendrán
    # Especificamos la cantidad de caracteres que contendrá el campo
    name = models.CharField(max_length=50)

    # Creamos un campo para asignar al usuario que creó el proyecto
    # Usamos el comando ForeignKey para relacionar el proyecto con otra tabla
    # Ponemos on_delete=models.CASCADE, Para que cuando se elimine un elemento, se eliminen también los que tienen una relación con el.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Definimos el método __str__ para que nos muestre el nombre del proyecto en el panel de administración
    def __str__(self):
        return self.name



# Crearemos una nueva clase que almacenara tareas
class task (models.Model):

    # Charfield nos sirve más para textos pequeños
    tittle = models.CharField(max_length=60)

    # Textfield nos sirve más para textos grandes
    # No especificamos la cantidad de caracteres que contendrá el campo
    description = models.TextField(blank=True)
    
    # Creamos un campo de fecha para definir la fecha de creación de la tarea
    created = models.DateTimeField(auto_now_add=True)
    
    # Creamos un campo para la fecha de completado de la tarea
    # Usamos el comando null para que acepte valores nulos
    datecompleted = models.DateTimeField(null=True, blank=True)
    
    # Creamos un campo para determinar su importancia
    important = models.BooleanField(default=False)
    
    # Creamos un campo para asignar al usuario que creó la tarea
    # Usamos el comando ForeignKey para relacionar la tarea con otra tabla
    # Ponemos on_delete=models.CASCADE, Para que cuando se elimine un elemento, se eliminen también los que tienen una relación con el.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Usamos el comando ForeignKey para relacionar la tarea con otra tabla
    # Ponemos on_delete=models.CASCADE, Para que cuando se elimine un elemento, se eliminen también los que tienen una relación con el.
    project = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    # Usamos el comando BooleanField para definir un campo booleano de las tareas
    done = models.BooleanField(default=False)  # Ponemos fFlse por defecto

    # Definimos el método __str__ para que nos muestre el nombre del proyecto en el panel de administración
    def __str__(self):
        return self.tittle + ' - ' + self.project.name + ' - by ' + self.user.username
    # Podemos agregar los otros campos como self.description
