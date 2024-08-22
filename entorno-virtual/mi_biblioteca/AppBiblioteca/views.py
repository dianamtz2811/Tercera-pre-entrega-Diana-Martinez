from django.shortcuts import render
from django.http import HttpResponse
from AppBiblioteca.models import Libro, Revista, Pelicula
from AppBiblioteca.forms import libroFormulario, revistaFormulario, peliculaFormulario

# Create your views here.
def inicio(request):
    return render(request, 'app_biblioteca/padre.html')

def libros(request):
    return render(request, 'app_biblioteca/libros.html')

def revistas(request):
    return render(request, 'app_biblioteca/revistas.html')

def peliculas(request):
    return render(request, 'app_biblioteca/peliculas.html')

def libro_Formulario(request):
    if request.method == 'POST':
        miFormulario = libroFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            libro = Libro (nombre=informacion['nombre'], autor=informacion['autor'])
            libro.save()
            return render(request, 'app_biblioteca/padre.html')
    else:
        miFormulario = libroFormulario()
    return render(request, 'app_biblioteca/libroFormulario.html', {"miFormulario": miFormulario})

def revista_Formulario(request):
    if request.method == 'POST':
        miFormulario = revistaFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            revista = Revista (nombre=informacion['nombre'], autor=informacion['autor'], año=informacion['año'])
            revista.save()
            return render(request, 'app_biblioteca/padre.html')
    else:
        miFormulario = revistaFormulario()
    return render(request, 'app_biblioteca/revistaFormulario.html', {"miFormulario": miFormulario})

def pelicula_Formulario(request):
    if request.method == 'POST':
        miFormulario = peliculaFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            pelicula = Pelicula (nombre=informacion['nombre'], director=informacion['director'], año=informacion['año'])
            pelicula.save()
            return render(request, 'app_biblioteca/padre.html')
    else:
        miFormulario = peliculaFormulario()
    return render(request, 'app_biblioteca/peliculaFormulario.html', {"miFormulario": miFormulario})

def busqueda_Director(request):
    return render(request, 'app_biblioteca/busquedaDirector.html')

def buscar(request):
    if request.GET['director']:
        director = request.GET['director']
        pelicula = Pelicula.objects.filter(director__icontains=director)
        return render(request, 'app_biblioteca/resultadosBusqueda.html', {'director':director})
    
    else:
        respuesta = "No enviste datos"
    
    return HttpResponse(respuesta)