# Utilizaremos el método POST para enviar los datos del formulario a la base de datos

# Importamor la libreria forms de django para poder crear un formulario
from django import forms

# Creamos una clase que hereda de forms.Form


class Createtask(forms.Form):

    # Creamos un campo de tipo CharField para el título de la tarea
    # Agregaremos estilos al formulario
    tittle = forms.CharField(label="Titulo de la tarea", max_length=60, widget=forms.TextInput(attrs={
        # Agregaremos estilos al formulario
        'class': 'form-control',
        'placeholder': 'Titulo de la tarea'}))

    # Creamos un campo de tipo CharField para la descripción de la tarea
    description = forms.CharField(
        label="Descripción de la tarea", widget=forms.Textarea(attrs={
            # Agregaremos estilos al formulario
            'class': 'form-control',
            'placeholder': 'Descripcion de la tarea',
            'rows': '3'}))

    # Creamos un campo para seleccionar el proyecto al que pertenece la tarea o crear uno nuevo proyecto


# Crearemos una clase para un formulario para crear un proyecto
class Createproject(forms.Form):

    # Creamos un campo de tipo CharField para el título del proyecto
    name = forms.CharField(label="Titulo del proyecto", max_length=50, 
    widget=forms.TextInput(attrs={
        # Agregaremos estilos al formulario
        'class': 'form-control',
        'placeholder': 'Nombre del proyecto'}))
