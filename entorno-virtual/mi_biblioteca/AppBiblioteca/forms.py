from django import forms
from AppBiblioteca.models import Libro

class libroFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    autor = forms.CharField()

class revistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    autor = forms.CharField()
    año = forms.CharField()

class peliculaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    director = forms.CharField()
    año = forms.CharField()

class Buscar(forms.Form):
    director = forms.CharField(max_length=20)


