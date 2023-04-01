# Este archivo nos servira para tener una mejor organización de las rutas de nuestra aplicación

# Importamos la función path
from django.urls import path

# Importamos las vistas de nuestra aplicación
from . import views # El punto indica que estamos en la misma carpeta


# Exportaremos las rutas de nuestra aplicación para que las podamos importar en el archivo urls.py de nuestro proyecto
# Exportamos una lista nueva
urlpatterns = [

    # Si dejamos la ruta vacia, nos enviara a la vista principal de nuestra aplicación
    path('', views.hello), # Otra forma de importar la vista es: path('', views.hello)

    # Llamamos a la segunda vista que hemos creado en views.py
    path('hello2/', views.hello2), # Para entrar a esta ruta, debemos escribir: /hello2/

    # Crearemos una ruta que esperará un parámetro usermane
    path('usernam/<str:username>', views.usernam), # Para entrar a esta ruta, debemos escribir: /home/hello3/username    

    # Crearemos una ruta que nos permita mostrar los proyectos que tenemos en nuestra base de datos
    path('projects/', views.projects), # Para entrar a esta ruta, debemos escribir: /projects/

    # Crearemos una ruta que nos permita mostrar las tareas que tenemos en nuestra base de datos
    path('tasks/', views.tasks), # Para entrar a esta ruta, debemos escribir: /tasks/

    # Creamos una ruta en donde el usuario podra crear una nueva tarea
    path('create_task/', views.create_task), # Para entrar a esta ruta, debemos escribir: /newtask/
]