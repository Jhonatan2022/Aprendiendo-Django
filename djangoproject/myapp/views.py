# En este documento podremos crear nuestras vistas o que le enviaremos a nuestro usuario

# Importamos la función render para poder crear una vista
from django.shortcuts import render

# Importamos el modelo http para poder crear una vista
# JsonResponse nos permite enviar datos en formato json
from django.http import HttpResponse, JsonResponse

# Importamos el modelo Proyecto para poder crear una vista de consultas
from .models import Proyecto, task  # Importamos el modelo Proyecto y task

# Importamos la función get_list_or_404 para poder crear una vista de error 404
# Importamos render para renderizar un template y redirect para redireccionar a una ruta
from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect

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

# Importamos un modelo para crear una fecha de comienzo y finalización
from django.utils import timezone

# Importamos login_required para que el usuario tenga que iniciar sesión para poder acceder a las rutas
from django.contrib.auth.decorators import login_required


# Create your views here.
# Crearemos una vista que para mostrar un mensaje en la página principal
def index(request):

    tittle = "!HI Welcome 👋"

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
@login_required
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
@login_required
def tasks(request):

    # Creamos una variable que nos permita e almacenamos los datos en una lista de diccionarios
    # tareas = task.objects.get(id = id) # Usamos el método get para obtener los datos de la tarea que coincida con el id que le pasamos por parámetro

    # tareas = get_object_or_404(task, id = id) # Usamos la función get_list_or_404 para obtener los datos y en caso de que no exista, nos muestre un error 404

    # Creamos una consulta para mostrarlos en la vista de los tamplates
    # Usamos el método all para obtener todos los datos de la tabla task
    # Creamos una consulta interna para que solo muestre las tareas del usuario actual
    # Pra filtrar las tareas no completadas completed__isnull=True
    tarea = task.objects.filter(user=request.user, datecompleted__isnull=True)

    # Imprimimos el id de la tarea que coincida con el id que le pasamos por parámetro
    return render(request, 'tasks/tasks.html', {
        'tasks': tarea
    })


# Creamos una vista para las tareas que estan completadas
@login_required
def completed_tasks(request):

    # Creamos una consulta para mostrarlos en la vista de los tamplates
    # Usamos el método all para obtener todos los datos de la tabla task
    # Creamos una consulta interna para que solo muestre las tareas del usuario actual
    # Pra filtrar las tareas completadas completed__isnull=False
    tarea = task.objects.filter(user=request.user, datecompleted__isnull=False).order_by(
        '-datecompleted')  # Usamos el método order_by para ordenar los datos de la tabla task

    # Imprimimos el id de la tarea que coincida con el id que le pasamos por parámetro
    return render(request, 'tasks/tasks.html', {
        'tasks': tarea
    })


# Creamos una vista para que el usuario pueda crear una nueva tarea
@login_required
def create_task(request):

    # Creamos una condicional para que si el usuario envia un formulario, nos guarde los datos en la base de datos.
    if request.method == 'GET':

        # Obtenemos todos los proyectos que pertenezcan al usuario actual
        # project = Proyecto.objects.filter(user=request.user)  

        

        return render(request, 'tasks/create_task.html', {
            'form': Createtask(),
            #'projects': project
        })
    # Creamos una condicional para que si el usuario envia un formulario, nos guarde los datos en la base de datos.
    else:

        # Metemos los parametro en un try en caso de que se generé un error
        try:
            # Creamos una variable que nos permita almacenar los datos que nos envia el usuario
            form = Createtask(request.POST)
            # Creamos una condicional para validar si el formulario es válido

            # Obtenemos todos los proyectos que pertenezcan al usuario actual
            # project = Proyecto.objects.filter(user=request.user)

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
                # 'projects': project,
                'error': 'No se ha podido crear la tarea :('
            })


# Creamos una vista para que el usuario pueda ver los detalles de una tarea
@login_required
def task_detail(request, task_id):

    # Utilizamos el taskform para que el usuario pueda editar los datos de la tarea
    if request.method == 'GET':

        # Usamos el método get para obtener los datos de la tarea que coincida con el id que le pasamos por parámetro
        # Creamos una consulta interna para que solo muestre las tareas del usuario actual
        tarea = get_object_or_404(task, pk=task_id, user=request.user)

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
            tarea = get_object_or_404(task, pk=task_id, user=request.user)

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

                # Mostramos un mensaje de error junto con el formulario
                'task': tarea,
                'form': form,
                'error': 'No se ha podido editar la tarea :('
            })


# Creamos una vista para que el usuario pueda marcar como completada una tarea
@login_required
def complete_task(request, task_id):

    # Creamos una variable que nos permita almacenar los datos que nos envia el usuario
    tarea = get_object_or_404(task, pk=task_id, user=request.user)

    # Creamos una condicional para validar si es por metodo GET o POST
    if request.method == 'POST':

        # Creamos el nuevo dato que vamos a guardar en la base de datos
        tarea.datecompleted = timezone.now()
        tarea.done = True

        # Guardamos los datos en la base de datos
        tarea.save()

        # Redireccionamos a la ruta tasks
        return redirect('tasks')


# Creamos una vista para que el usuario pueda eliminar una tarea
@login_required
def delete_task(request, task_id):

    # Creamos una variable que nos permita almacenar los datos que nos envia el usuario
    tarea = get_object_or_404(task, pk=task_id, user=request.user)

    # Creamos una condicional para validar si es por metodo GET o POST
    if request.method == 'POST':

        # Eliminamos los datos de la base de datos
        tarea.delete()

        # Redireccionamos a la ruta tasks
        return redirect('tasks')


# Creamos una vista que nos permita mostrar los proyectos que tenemos en nuestra base de datos
@login_required
def projects(request):

    # Creamos una variable que nos permita e almacenamos los datos en una lista de diccionarios
    # proyectos = list(Proyecto.objects.values()) # values() nos permite obtener los valores de los campos de la tabla Proyecto

    # Crearemos una consulta para mostrarlos en la vista de los tamplates
    # Usamos el metodo filter para filtrar los datos que coincidan con el usuario actual
    datosprojects = Proyecto.objects.filter(user=request.user)

    # Imprimimos los proyectos que tenemos en nuestra base de datos
    return render(request, 'projects/projects.html', {
        'projects': datosprojects
    })  # safe=False nos permite enviar datos en formato json


# Creamos una vista para que el usuario pueda crear un nuevo proyecto
@login_required
def create_project(request):

    # Creamos una condicional para que si el usuario envia un formulario, nos guarde los datos en la base de datos.
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': Createproject()
        })

    # En caso de que el usuario envie un formulario, nos guarde los datos en la base de datos
    else:

        # Metemos el metodo en un try en caso de que se genere un error
        try:
            # Creamos una variable que nos permita almacenar los datos que nos envia el usuario
            new_project = Createproject(request.POST)

            # Creamos una variable que nos permita almacenar los datos que nos envia el usuario
            new_project = new_project.save(commit=False)

            # Asignamos el proyecto al usuario actual
            new_project.user = request.user

            # Guardamos los datos en la base de datos
            new_project.save()

            # Redireccionamos a la ruta projects
            return redirect('projects')

        # En caso de que se genere un error, nos redirecciona a la ruta create_project
        except ValueError:

            # Renderizamos el formulario con un mensaje de error
            return render(request, 'projects/create_project.html', {
                'form': Createproject(),
                'error': 'No se ha podido crear el proyecto :('
            })


# Creamos una vista para que el usuario pueda eliminar un proyecto
@login_required
def delete_project(request, pro_id):

    # Creamos una variable que nos permita almacenar los datos que nos envia el usuario
    project = get_object_or_404(Proyecto, pk=pro_id, user=request.user)

    # Creamos una condicional para validar si es por metodo GET o POST
    if request.method == 'POST':

        # Eliminamos los datos de la base de datos
        project.delete()

        # Redireccionamos a la ruta projects
        return redirect('projects')


# Creamos una vista unica para mostrar los datos de un projecto
@login_required
def project_detail(request, id):

    # Utilizamos el createproject para que nos muestre los datos del proyecto y los pueda editar

    if request.method == 'GET':

        # Creamos una variable que nos permita almacenar los datos que nos envia el usuario
        projecto = get_object_or_404(Proyecto, pk=id, user=request.user)

        form = Createproject(instance=projecto)
        # Renderizamos el template project_detail.html
        return render(request, 'projects/detail.html', {

            # Creamos un formulario de actualización de datos
            'project': projecto,
            'form': form
        })
    else:

        # Metemos el metodo en un try en caso de que se genere un error
        try:
            # Creamos una variable que nos permita almacenar los datos que nos envia el usuario
            projecto = get_object_or_404(Proyecto, pk=id, user=request.user)

            # Creamos una variable que nos permita almacenar los datos que nos envia el usuario
            form = Createproject(request.POST, instance=projecto)

            # Guardamos los datos en la base de datos
            form.save()

            # Redireccionamos a la ruta projects
            return redirect('projects')

        # En caso de que se genere un error, nos redirecciona a la ruta create_project
        except ValueError:
            # Renderizamos el formulario con un mensaje de error
            return render(request, 'projects/detail.html', {

                # Creamos un formulario de actualización de datos junto con el mensaje de error
                'project': projecto,
                'form': form,
                'error': 'No se ha podido editar el proyecto :('
            })
        