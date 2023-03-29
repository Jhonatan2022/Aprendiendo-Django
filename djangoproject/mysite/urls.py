"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # Utilizando include podremos importar las rutas de nuestra aplicación


# Importamos la vista que hemos creado en views.py
#from myapp import views # Otra forma de importar la vista es:  from myapp.views import hello

# En este apartado pondremos las rutas del proyecto que los usuarios podran acceder
urlpatterns = [
    path('admin/', admin.site.urls),

    # Importamos las rutas de nuestra aplicación
    # Podemos agregarle un prefijo a las rutas de nuestra aplicación con el argumento 'home/'
    path('', include('myapp.urls')), # Dejamos la ruta vacia para que nos muestre la vista principal de nuestra aplicación para no tener que poner rutas precedentes
]