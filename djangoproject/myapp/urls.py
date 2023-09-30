from django.urls import path
from . import views  # El punto indica que estamos en la misma carpeta
from django.conf import settings
from django.contrib.staticfiles.urls import static


# Exportamos una lista nueva
urlpatterns = [
    # Si dejamos la ruta vacia, nos enviara a la vista principal de nuestra aplicación
    # Otra forma de importar la vista es: path('', views.hello)
    path("", views.index, name="index"),  # Asignamos un nombre a la ruta
    # Creamos una ruta que nos permita mostrar el formulario de registro
    # Asignamos un nombre a la ruta
    path("singup/", views.singup, name="singup"),
    # Crearemos una ruta para el cierre de sesión del usuario
    # Asignamos un nombre a la ruta
    path("logout/", views.singout, name="logout"),
    # Crearemos una ruta para el inicio de sesión del usuario
    # Asignamos un nombre a la ruta
    path("login/", views.login_user, name="login"),
    # Crearemos una ruta que nos permita mostrar los proyectos que tenemos en nuestra base de datos
    # Creamos una ruta en donde el usuario podra crear un proyecto
    # Para entrar a esta ruta, debemos escribir: /edit_project/id
    path(
        "create_project/", views.create_project, name="createproject"
    ),  # Asignamos nombre a la ruta
    # Para entrar a esta ruta, debemos escribir: /projects/
    # Asignamos nombre a la ruta
    path("projects/", views.projects, name="projects"),
    # Creamos una ruta donde el usuario podra eliminar un proyecto
    # Para entrar a esta ruta, debemos escribir: /delete_project/id
    path("projects/<int:pro_id>/delete", views.delete_project, name="delete_project"),
    # Creamos una ruta donde el usuario pofrá ver los detalles del un proyecto
    path(
        "projects/<int:id>", views.project_detail, name="projectdetail"
    ),  # Asignamos nombre a la ruta
    # Crearemos una ruta que nos permita mostrar las tareas que tenemos en nuestra base de datos
    # Para entrar a esta ruta, debemos escribir: /tasks/
    path("tasks/", views.tasks, name="tasks"),  # Asignamos nombre a la ruta
    # Creamos una ruta en donde el usuario podra crear una nueva tarea
    # Para entrar a esta ruta, debemos escribir: /newtask/
    # Asignamos nombre a la ruta
    path("tasks/create_task/", views.create_task, name="createtask"),
    # Creamos una ruda donde el usuario podra ver los detalles de una tarea
    # Para entrar a esta ruta, debemos escribir: /task/id
    # Asignamos nombre a la ruta
    path("tasks/<int:task_id>/", views.task_detail, name="taskdetail"),
    # Creamos una ruta donde el usuario marque una tarea como completada
    # Para entrar a esta ruta, debemos escribir: /task/complete/id
    # Asignamos nombre a la ruta
    path("tasks/<int:task_id>/complete", views.complete_task, name="complete_task"),
    # Creamos una ruta donde el usuario pueda eliminar una tarea
    # Para entrar a esta ruta, debemos escribir: /task/delete/id
    # Asignamos nombre a la ruta
    path("tasks/<int:task_id>/delete", views.delete_task, name="delete_task"),
    # Creamos una ruta para las tareas completadas
    # Para entrar a esta ruta, debemos escribir: /tasks/completed/
    # Asignamos nombre a la ruta
    path("tasks/completed/", views.completed_tasks, name="completed_tasks"),
    # Agregamos la carga de archivos estaticos
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
