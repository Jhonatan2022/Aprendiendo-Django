# En este documento podremos crear nuestras vistas o que le enviaremos a nuestro usuario

from django.shortcuts import render
# Importamos el modelo http para poder crear una vista
from django.http import HttpResponse

# Create your views here.

# Crearemos una vista que nos permita mostrar un mensaje en la página principal de nuestra aplicación
def hello(request):
    return HttpResponse("<h1> Hello World </h1>")

# Creamos una segunda vista que nos permita mostrar un mensaje en la página principal de nuestra aplicación
def hello2(request):
    return HttpResponse("<h1> Second hello world </h1>")