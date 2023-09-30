# Utilizaremos el método POST para enviar los datos del formulario a la base de datos

# Importamor la libreria forms de django para poder crear un formulario
from django import forms

# Importamos el modelo task
from .models import task, Proyecto

# Importamos el modulo que contiene la clase User
from django.contrib.auth.models import User


# Creamos una clase que hereda de forms.Form
class Createtask(forms.ModelForm):
    class Meta:
        # Definimos el modelo al que pertenece el formulario
        model = task

        # Definimos los campos que tendrá el formulario
        fields = ["tittle", "description", "project", "important"]

        # Agregaremos estilos al formulario
        widgets = {
            # Agregaremos estilos al formulario
            "tittle": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Write tittle of task",
                }
            ),
            "image": forms.FileInput(attrs={"class": "form-control mb-3"}),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Write description of task",
                    "rows": "3",
                }
            ),
            "project": forms.Select(attrs={"class": "form-select mb-3"}),
            "important": forms.CheckboxInput(attrs={"class": "form-check-input mb-3"}),
        }


# Crearemos una clase para un formulario para crear un proyecto
class Createproject(forms.ModelForm):
    class Meta:
        # Definimos el modelo al que pertenece el formulario
        model = Proyecto
        fields = ["name"]