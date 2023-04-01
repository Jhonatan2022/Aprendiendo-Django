# Este archivo contiene los modelos de la aplicación en donde podremos crear clases que representen a las tablas de nuestra base de datos.

# Usaremos principlamente la clase models.py para proyectos y tareas
from django.db import models

# Create your models here.


class Proyecto(models.Model):
    # Definimos los campos de la tabla Proyecto y los tipos de datos que contendrán
    # Especificamos la cantidad de caracteres que contendrá el campo
    name = models.CharField(max_length=50)

    # Definimos el método __str__ para que nos muestre el nombre del proyecto en el panel de administración
    def __str__(self):
        return self.name

# Crearemos una nueva clase que almacenara tareas


class task (models.Model):
    # Charfield nos sirve más para textos pequeños
    tittle = models.CharField(max_length=60)

    # Textfield nos sirve más para textos grandes
    # No especificamos la cantidad de caracteres que contendrá el campo
    description = models.TextField()

    # Usamos el comando ForeignKey para relacionar la tarea con otra tabla
    # Ponemos on_delete=models.CASCADE, Para que cuando se elimine un elemento, se eliminen también los que tienen una relación con el.
    project = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    # Usamos el comando BooleanField para definir un campo booleano de las tareas
    done = models.BooleanField(default=False)  # Ponemos fFlse por defecto

    # Definimos el método __str__ para que nos muestre el nombre del proyecto en el panel de administración
    def __str__(self):
        return self.tittle + ' - ' + self.project.name
    # Podemos agregar los otros campos como self.description
