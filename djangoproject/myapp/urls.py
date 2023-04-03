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
    path('', views.hello, name="index"), # Asignamos un nombre a la ruta

    # Llamamos a la segunda vista que hemos creado en views.py
    # Para entrar a esta ruta, debemos escribir: /hello2/
    path('hello2/', views.hello2, name="index2"), # Asignamos un nombre a la ruta

    # Crearemos una ruta que esperará un parámetro usermane
    # Para entrar a esta ruta, debemos escribir: /home/hello3/username
    path('usernam/<str:username>', views.usernam, name="username"), #Asignamos nombre a la ruta

    # Crearemos una ruta que nos permita mostrar los proyectos que tenemos en nuestra base de datos
    
    # Creamos una ruta en donde el usuario podra crear un proyecto
    # Para entrar a esta ruta, debemos escribir: /edit_project/id
    path('create_project/', views.create_project, name="createproject"), # Asignamos nombre a la ruta


    # Para entrar a esta ruta, debemos escribir: /projects/
    path('projects/', views.projects, name="projects"), # Asignamos nombre a la ruta
    
    # Creamos una ruta donde el usuario pofrá ver los detalles del un proyecto
    path('projects/<int:id>', views.project_detail, name="projectdetail"), # Asignamos nombre a la ruta


    # Crearemos una ruta que nos permita mostrar las tareas que tenemos en nuestra base de datos
    # Para entrar a esta ruta, debemos escribir: /tasks/
    path('tasks/', views.tasks, name="tasks"), # Asignamos nombre a la ruta

    # Creamos una ruta en donde el usuario podra crear una nueva tarea
    # Para entrar a esta ruta, debemos escribir: /newtask/
    path('create_task/', views.create_task, name="createtask"), # Asignamos nombre a la ruta   
]
