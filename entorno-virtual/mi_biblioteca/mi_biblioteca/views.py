from django.http import HttpResponse
from django.template import loader
from AppBiblioteca.models import Libro, Revista, Pelicula

def agregar_libro (request, nom, aut):
    libro = Libro(nombre=nom, autor=aut)
    libro.save()
    return HttpResponse(f'Libro agregado: {nom} de {aut}')

def agregar_revista(request, nom, aut, año):
    revista = Revista(nombre=nom, autor=aut, año=año)
    revista.save()
    return HttpResponse(f'Revista agregada: {nom} de {aut} del año {año}')

def agregar_pelicula(request, nom, dir, año):
    pelicula = Pelicula(nombre=nom, director=dir, año=año)
    pelicula.save()
    return HttpResponse(f'Pelicula agregada: {nom} de {dir} del año {año}')
