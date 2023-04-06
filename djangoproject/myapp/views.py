# En este documento podremos crear nuestras vistas o que le enviaremos a nuestro usuario

# Importamos la función render para poder crear una vista
from django.shortcuts import render

# Importamos el modelo http para poder crear una vista
# JsonResponse nos permite enviar datos en formato json
from django.http import HttpResponse, JsonResponse

# Importamos el modelo Proyecto para poder crear una vista de consultas
from .models import Proyecto, task  # Importamos el modelo Proyecto y task

# Importamos la función get_list_or_404 para poder crear una vista de error 404
from django.shortcuts import get_object_or_404, get_list_or_404

# Importamos render para renderizar un template y redirect para redireccionar a una ruta
from django.shortcuts import render, redirect

# Importamos el formulario que hemos creado en forms.py
# Importamos el formulario Createtask y createproject
from .forms import Createtask, Createproject

# Importamos un modelo para crear un formulario de registro
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# IMportamos un modelo para crear usuarios
from django.contrib.auth.models import User

# Importamos un modelo para certificar el token del usuario
from django.contrib.auth import login, logout, authenticate

# Importamos un modelo para validar errores especificos
from django.db import IntegrityError


# Create your views here.
# Crearemos una vista que para mostrar un mensaje en la página principal
def index(request):

    tittle = "Welcome to my first Django project"

    # Creamos una variable para almacenar le nombre del usuario logueado
    nameuser = (request.user)

    # Creamos un render que nos permita mostrar un template en la página principal de nuestra aplicación
    return render(request, "index.html", {
        "titulo": tittle,
        "nameuser": nameuser
    })


# Creamos una vista que en donde el usuario podrá registrarse
def singup(request):

    # Creamos una condicional para que si el usuario envia un formulario, nos guarde los datos en la base de datos.
    if request.method == 'GET':
        # Renderizamos el formulario de registro en caso de que el usuario no envie un formulario
        return render(request, "singup.html", {

            # Creamos un formulario de registro que suministra Django
            "form": UserCreationForm()
        })
    else:
        # Creamos una condicional para validad que las contraseñas coincidan
        if request.POST['password1'] == request.POST['password2']:

            # Creamos un try para que si el usuario ya existe, nos muestre un mensaje de error o en caso de un error por la base de datos
            try:
                # Creamos un nuevo usuario y le pasamos los datos que nos envia el usuario
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])

                # Guardamos los datos del usuario en la base de datos
                user.save()

                # Creamos una sesión para el usuario
                login(request, user)

                # Mostramos un mensaje de que el usuario ha sido creado correctamente
                # return HttpResponse("<h1> Usuario creado correctamente </h1>")
                # Redireccionamos a la ruta index
                return redirect('index')

            except IntegrityError:
                # En caso de que el usuario ya exista, nos redirecciona a la ruta singup
                # Renderizamos el formulario de registro en caso de que el usuario no envie un formulario
                return render(request, "singup.html", {

                    # Creamos un formulario de registro que suministra Django
                    "form": UserCreationForm(),
                    "error": "El nombre de usuario ya existe"
                })

        # En caso de que las contraseñas no coincidan, nos redirecciona a la ruta singup
        # Renderizamos el formulario de registro en caso de que el usuario no envie un formulario
        return render(request, "singup.html", {

            # Creamos un formulario de registro que suministra Django
            "form": UserCreationForm(),
            "error": "Las contraseñas no coinciden"
        })


# Creamos una función para que el usuario pueda cerrar sesión
def singout(request):

    # Cerramos la sesión del usuario
    logout(request)

    # Redireccionamos a la ruta index
    return redirect('index')


# Creamos una vista para que el usuario pueda iniciar sesión
def login_user(request):

    # Creamos una condicional para que si el usuario envia un formulario, nos guarde los datos en la base de datos.
    if request.method == 'GET':
        # Renderizamos el formulario de inicio de sesión
        return render(request, "login.html", {
            # Creamos un formulario de inicio de sesión que suministra Django
            "form": AuthenticationForm()
        })
    else:
        # Auntentificamos si el usuario existe en la base de datos
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        # Creamos una condicional para validar si el usuario existe en la base de datos
        if user is None:
            # Renderizamos el formulario de inicio de sesión
            return render(request, "login.html", {
                # Creamos un formulario de inicio de sesión que suministra Django
                "form": AuthenticationForm(),
                "error": "El nombre de usuario o la contraseña son incorrectos"
            })
        # En caso de que el usuario exista en la base de datos creamos una sesión para el usuario
        else:
            # Creamos una sesión para el usuario
            login(request, user)

            # Redireccionamos a la ruta index
            return redirect('index')


# Creamos una vista que nos permita mostrar las tareas que tenemos en nuestra base de datos
def tasks(request):

    # Creamos una variable que nos permita e almacenamos los datos en una lista de diccionarios
    # tareas = task.objects.get(id = id) # Usamos el método get para obtener los datos de la tarea que coincida con el id que le pasamos por parámetro

    # tareas = get_object_or_404(task, id = id) # Usamos la función get_list_or_404 para obtener los datos y en caso de que no exista, nos muestre un error 404

    # Creamos una consulta para mostrarlos en la vista de los tamplates
    # Usamos el método all para obtener todos los datos de la tabla task
    # Creamos una consulta interna para que solo muestre las tareas del usuario actual
    # Pra filtrar las tareas no completadas completed__isnull=True
    tarea = task.objects.filter(user=request.user)

    # Imprimimos el id de la tarea que coincida con el id que le pasamos por parámetro
    return render(request, 'tasks/tasks.html', {
        'tasks': tarea
    })


# Creamos una vista para que el usuario pueda crear una nueva tarea
def create_task(request):

    # Creamos una condicional para que si el usuario envia un formulario, nos guarde los datos en la base de datos.
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': Createtask()
        })
    # Creamos una condicional para que si el usuario envia un formulario, nos guarde los datos en la base de datos.
    else:

        # Metemos los parametro en un try en caso de que se generé un error
        try:
            # Creamos una variable que nos permita almacenar los datos que nos envia el usuario
            form = Createtask(request.POST)
            # Creamos una condicional para validar si el formulario es válido

            # Creamos una variable que nos permita almacenar los datos que nos envia el usuario
            new_task = form.save(commit=False)
            # Asignamos la tarea a un usuario
            new_task.user = request.user

            # Guardamos los datos en la base de datos
            new_task.save()

            # Redireccionamos a la ruta tasks
            return redirect('tasks')

        # En caso de que se genere un error, nos redirecciona a la ruta create_task
        except ValueError:
            # Renderizamos el formulario de registro en caso de que el usuario no envie un formulario
            return render(request, 'tasks/create_task.html', {
                'form': Createtask(),
                'error': 'No se ha podido crear la tarea :('
            })


# Creamos una vista para que el usuario pueda ver los detalles de una tarea
def task_detail(request, id):

    # Utilizamos el taskform para que el usuario pueda editar los datos de la tarea
    if request.method == 'GET':

        # Usamos el método get para obtener los datos de la tarea que coincida con el id que le pasamos por parámetro
        # Creamos una consulta interna para que solo muestre las tareas del usuario actual
        tarea = get_object_or_404(task, pk=id)

        # Insertamos los datos de la tarea en el formulario
        form = Createtask(instance=tarea)

        # Renderizamos el formulario con los datos de la tarea
        return render(request, 'tasks/task_detail.html', {

            # Creamos un formulario de actualización de datos
            'task': tarea,
            'form': form
        })
    else:
        try:

            tarea = get_object_or_404(task, pk=id)

            # Creamos una variable que nos permita almacenar los datos que nos envia el usuario
            form = Createtask(request.POST, instance=tarea)

            # Guardamos los datos en la base de datos
            form.save()

            # Redireccionamos a la ruta tasks
            return redirect('tasks')

        # En caso de que se genere un error, nos redirecciona a la ruta create_task
        except ValueError:
            # Renderizamos el formulario de registro en caso de que el usuario no envie un formulario
            return render(request, 'tasks/task_detail.html', {
                'task': tarea,
                'form': form,
                'error': 'No se ha podido editar la tarea :('
            })


# Creamos una vista que nos permita mostrar los proyectos que tenemos en nuestra base de datos
def projects(request):

    # Creamos una variable que nos permita e almacenamos los datos en una lista de diccionarios
    # proyectos = list(Proyecto.objects.values()) # values() nos permite obtener los valores de los campos de la tabla Proyecto

    # Crearemos una consulta para mostrarlos en la vista de los tamplates
    # Usamos el método all para obtener todos los datos de la tabla Proyecto
    datosprojects = Proyecto.objects.all()

    # Imprimimos los proyectos que tenemos en nuestra base de datos
    return render(request, 'projects/projects.html', {
        'projects': datosprojects
    })  # safe=False nos permite enviar datos en formato json


# Creamos una vista para que el usuario pueda crear un nuevo proyecto
def create_project(request):

    # Creamos una condicional para que si el usuario envia un formulario, nos guarde los datos en la base de datos.
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': Createproject()
        })

    # En caso de que el usuario envie un formulario, nos guarde los datos en la base de datos
    else:
        # Creamos un nuevo proyecto y le pasamos los datos que nos envia el usuario
        Proyecto.objects.create(name=request.POST['name'])

    # Redireccionamos a la ruta projects
    return redirect('projects')


# Creamos una vista unica para mostrar los datos de un projecto
def project_detail(request, id):
    # Creamos una consulta para mostrarlos en la vista de los tamplates
    # Usamos el método all para obtener todos los datos de la tabla Proyecto

    # Lanzamos un pagina de error 404 en caso de que no exista el proyecto
    datosprojects = get_object_or_404(Proyecto, id=id)

    # Hacemos una consulta para obtener los datos de las tareas que coincidan con el id del proyecto
    tasks = task.objects.filter(project_id=id)

    # Renderizamos el template project_detail.html
    return render(request, 'projects/detail.html', {
        'project': datosprojects,
        'tasks': tasks

    })
