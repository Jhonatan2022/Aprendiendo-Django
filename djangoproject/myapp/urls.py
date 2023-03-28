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
    path('hello2/', views.hello2),
]