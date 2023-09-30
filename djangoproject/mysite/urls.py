from django.contrib import admin
from django.urls import path, include


# En este apartado pondremos las rutas del proyecto que los usuarios podran acceder
urlpatterns = [
    path("admin/", admin.site.urls),
    # Importamos las rutas de nuestra aplicación
    # Podemos agregarle un prefijo a las rutas de nuestra aplicación con el argumento 'home/'
    # Dejamos la ruta vacia para que nos muestre la vista principal de nuestra aplicación para no tener que poner rutas precedentes
    path("", include("myapp.urls")),
]
