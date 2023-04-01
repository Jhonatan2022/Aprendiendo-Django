# En este documento podremos crear nuestras vistas o que le enviaremos a nuestro usuario

# Importamos la función render para poder crear una vista
from django.shortcuts import render
# Importamos el modelo http para poder crear una vista
from django.http import HttpResponse, JsonResponse # JsonResponse nos permite enviar datos en formato json
# Importamos el modelo Proyecto para poder crear una vista de consultas
from .models import Proyecto, task # Importamos el modelo Proyecto y task
from django.shortcuts import get_object_or_404 # Importamos la función get_list_or_404 para poder crear una vista de error 404 
from django.shortcuts import render, redirect # Importamos render para renderizar un template y redirect para redireccionar a una ruta
# Importamos el formulario que hemos creado en forms.py
from .forms import Createtask

# Create your views here.

# Crearemos una vista que nos permita mostrar un mensaje en la página principal de nuestra aplicación
def hello(request):

    tittle = "Welcome to my first Django project"
    # Creamos un render que nos permita mostrar un template en la página principal de nuestra aplicación
    return render(request, "index.html", {
        "titulo": tittle
    })


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
        # proyectos = list(Proyecto.objects.values()) # values() nos permite obtener los valores de los campos de la tabla Proyecto

        # Crearemos una consulta para mostrarlos en la vista de los tamplates
        datosprojects = Proyecto.objects.all() # Usamos el método all para obtener todos los datos de la tabla Proyecto

        # Imprimimos los proyectos que tenemos en nuestra base de datos
        return render(request, 'projects.html', {
             'projects': datosprojects
        }) # safe=False nos permite enviar datos en formato json


# Creamos una vista que nos permita mostrar las tareas que tenemos en nuestra base de datos
def tasks(request):
        
        # Creamos una variable que nos permita e almacenamos los datos en una lista de diccionarios
        # tareas = task.objects.get(id = id) # Usamos el método get para obtener los datos de la tarea que coincida con el id que le pasamos por parámetro

        # tareas = get_object_or_404(task, id = id) # Usamos la función get_list_or_404 para obtener los datos y en caso de que no exista, nos muestre un error 404

        # Creamos una consulta para mostrarlos en la vista de los tamplates
        taks = task.objects.all() # Usamos el método all para obtener todos los datos de la tabla task

        # Imprimimos el id de la tarea que coincida con el id que le pasamos por parámetro
        return render(request, 'tasks.html', {
            'tasks': taks
        })


# Creamos una vista para que el usuario pueda crear una nueva tarea
def create_task(request):
     
    # Creamos una condicional para que si el usuario envia un formulario, nos guarde los datos en la base de datos.
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': Createtask()
        })
    else: 
        task.objects.create(tittle = request.POST['tittle'], 
                            description = request.POST['description'],
                            status = request.POST['status'],
                            project = request.POST['project'])
        return redirect('tasks/')