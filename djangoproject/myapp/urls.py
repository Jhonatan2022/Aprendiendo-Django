# Este archivo nos servira para tener una mejor organización de las rutas de nuestra aplicación

# Importamos la función path
from django.urls import path

# Importamos las vistas de nuestra aplicación
from . import views  # El punto indica que estamos en la misma carpeta


# Exportaremos las rutas de nuestra aplicación para que las podamos importar en el archivo urls.py de nuestro proyecto
# Exportamos una lista nueva
urlpatterns = [

    # Si dejamos la ruta vacia, nos enviara a la vista principal de nuestra aplicación
    # Otra forma de importar la vista es: path('', views.hello)
    path('', views.index, name="index"),  # Asignamos un nombre a la ruta


    # Creamos una ruta que nos permita mostrar el formulario de registro
    # Asignamos un nombre a la ruta
    path('singup/', views.singup, name='singup'),


    # Crearemos una ruta para el cierre de sesión del usuario
    # Asignamos un nombre a la ruta
    path('logout/', views.singout, name='logout'),


    # Crearemos una ruta para el inicio de sesión del usuario
    # Asignamos un nombre a la ruta
    path('login/', views.login_user, name='login'),


    # Crearemos una ruta que nos permita mostrar los proyectos que tenemos en nuestra base de datos
    # Creamos una ruta en donde el usuario podra crear un proyecto
    # Para entrar a esta ruta, debemos escribir: /edit_project/id
    path('create_project/', views.create_project,
         name="createproject"),  # Asignamos nombre a la ruta


    # Para entrar a esta ruta, debemos escribir: /projects/
    # Asignamos nombre a la ruta
    path('projects/', views.projects, name="projects"),


    # Creamos una ruta donde el usuario pofrá ver los detalles del un proyecto
    path('projects/<int:id>', views.project_detail,
         name="projectdetail"),  # Asignamos nombre a la ruta


    # Crearemos una ruta que nos permita mostrar las tareas que tenemos en nuestra base de datos
    # Para entrar a esta ruta, debemos escribir: /tasks/
    path('tasks/', views.tasks, name="tasks"),  # Asignamos nombre a la ruta


    # Creamos una ruta en donde el usuario podra crear una nueva tarea
    # Para entrar a esta ruta, debemos escribir: /newtask/
    # Asignamos nombre a la ruta
    path('create_task/', views.create_task, name="createtask"),


]
