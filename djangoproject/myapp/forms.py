# Utilizaremos el método POST para enviar los datos del formulario a la base de datos

# Importamor la libreria forms de django para poder crear un formulario
from django import forms

# Creamos una clase que hereda de forms.Form
class Createtask(forms.Form):

    tittle = forms.CharField(label="Titulo de la tarea", max_length=60) # Creamos un campo de tipo CharField para el título de la tarea

    description = forms.CharField(label="Descripción de la tarea", widget=forms.Textarea) # Creamos un campo de tipo CharField para la descripción de la tarea

