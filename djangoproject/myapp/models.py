# Este archivo contiene los modelos de la aplicación en donde podremos crear clases que representen a las tablas de nuestra base de datos.

# Usaremos principlamente la clase models.py para proyectos y tareas
from django.db import models

# Create your models here.
class Proyecto(models.Model):
    # Definimos los campos de la tabla Proyecto y los tipos de datos que contendrán
    name = models.CharField(max_length=50) # Especificamos la cantidad de caracteres que contendrá el campo


# Crearemos una nueva clase que almacenara tareas
class task (models.Model): 
    # Charfield nos sirve más para textos pequeños
    tittle = models.CharField (max_length=60)

    # Textfield nos sirve más para textos grandes
    description = models.TextField () # No especificamos la cantidad de caracteres que contendrá el campo

    # Usamos el comando ForeignKey para relacionar la tarea con otra tabla
    project = models.ForeignKey (Proyecto, on_delete=models.CASCADE) # Ponemos on_delete=models.CASCADE, Para que cuando se elimine un elemento, se eliminen también los que tienen una relación con el.