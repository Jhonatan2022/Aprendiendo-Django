# En este documento podremos crear nuestras vistas o que le enviaremos a nuestro usuario

# Importamos la función render para poder crear una vista
from django.shortcuts import render
# Importamos el modelo http para poder crear una vista
from django.http import HttpResponse, JsonResponse # JsonResponse nos permite enviar datos en formato json
# Importamos el modelo Proyecto para poder crear una vista de consultas
from .models import Proyecto, task # Importamos el modelo Proyecto y task
from django.shortcuts import get_object_or_404 # Importamos la función get_list_or_404 para poder crear una vista de error 404 

# Create your views here.

# Crearemos una vista que nos permita mostrar un mensaje en la página principal de nuestra aplicación
def hello(request):
    return HttpResponse("<h1> Hello World </h1>")


# Creamos una vista que nos permita mostrar un mensaje en la página principal de nuestra aplicación
def hello2(request):
    return HttpResponse("<h1> Second hello world </h1>")


# Creamos una vista que nos permita mostras un mensaje de bienvenida al usuario
def usernam(request, username):

    # Creamos una condición para que si el usuario no ingresa un nombre, nos muestre un mensaje de error
    if username == '':
        return HttpResponse("<h1> Error, no has ingresado un nombre </h1>")
    
    # Mostremos un mensaje de bienvenida al usuario
    weolcome = username + " this is my first Django project"

    # Retornamos el mensaje de bienvenida y concatenamos el nombre del usuario
    return HttpResponse("<h1> Welcome %s </h1>" %weolcome)


# Creamos una vista que nos permita mostrar los proyectos que tenemos en nuestra base de datos
def projects(request):
    
        # Creamos una variable que nos permita e almacenamos los datos en una lista de diccionarios
        proyectos = list(Proyecto.objects.values()) # values() nos permite obtener los valores de los campos de la tabla Proyecto

        
        # Imprimimos los proyectos que tenemos en nuestra base de datos
        return JsonResponse(proyectos, safe=False) # safe=False nos permite enviar datos en formato json


# Creamos una vista que nos permita mostrar las tareas que tenemos en nuestra base de datos
def tasks(request, id):
        
        # Creamos una variable que nos permita e almacenamos los datos en una lista de diccionarios
        # tareas = task.objects.get(id = id) # Usamos el método get para obtener los datos de la tarea que coincida con el id que le pasamos por parámetro

        tareas = get_object_or_404(task, id = id) # Usamos la función get_list_or_404 para obtener los datos y en caso de que no exista, nos muestre un error 404

        # Imprimimos el id de la tarea que coincida con el id que le pasamos por parámetro
        return HttpResponse ('The tittle of the task is: %s '  %tareas.tittle)