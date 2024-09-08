from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from AppBiblioteca.models import Libro, Revista, Pelicula
from AppBiblioteca.forms import libroFormulario, revistaFormulario, peliculaFormulario
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, 'app_biblioteca/padre.html')

@login_required
def libros(request):
    return render(request, 'app_biblioteca/libros.html')

@login_required
def revistas(request):
    return render(request, 'app_biblioteca/revistas.html')

@login_required
def peliculas(request):
    return render(request, 'app_biblioteca/peliculas.html')

@login_required
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

@login_required
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

@login_required
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

@login_required
def busqueda_Director(request):
    return render(request, 'app_biblioteca/busquedaDirector.html')

@login_required
def buscar(request):
    if request.GET['director']:
        director = request.GET['director']
        pelicula = Pelicula.objects.filter(director__icontains=director)
        return render(request, 'app_biblioteca/resultadosBusqueda.html', {'director':director, 'peliculas':pelicula})
    
    else:
        respuesta = "No enviste datos"
    
    return HttpResponse(respuesta)

@login_required
def leerLibros(request):
    libro = Libro.objects.all()
    contexto = {"libro": libro}
    return render (request, 'app_biblioteca/leerLibros.html', contexto)

@login_required
def eliminarLibro(request, libro_nombre):
    libro = Libro.objects.get(nombre=libro_nombre)
    libro.delete()

    libro = Libro.objects.all()
    contexto = {"libro": libro}
    return render(request, 'app_biblioteca/leerLibros.html', contexto)

class LibrosListView(LoginRequiredMixin, ListView): 
    #Vista para mostrar una lista de todos los libros
    model = Libro
    context_object_name="libros"
    template_name = "app_biblioteca/librosList.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class LibrosDetailView(LoginRequiredMixin, DetailView):
    #Vista para mostrar los detalles de un libro en particular
    model = Libro
    context_object_name = "libros"
    template_name = "app_biblioteca/librosDetail.html"

    def get_object(self):
        return get_object_or_404(Libro, nombre=self.kwargs['nombre'])

class LibroCreateView(CreateView):
    #Vista para agregar nuevos libros a través de un formulario
    model = Libro
    template_name = "app_biblioteca/librosForm.html"
    success_url = reverse_lazy('librosList') #URL de redireccion después de crear el curso
    fields = ["nombre", "autor"]

class LibroUpdateView(UpdateView):
    #Vista para actualizar los datos de un libro existente
    model = Libro
    template_name = "app_biblioteca/librosUpdate.html"
    success_url = reverse_lazy('librosList')
    fields = ["nombre", "autor"]

    def get_object(self):
        nombre = self.kwargs.get("nombre")
        return Libro.objects.get(nombre=nombre)

class LibroDeleteView(DeleteView):
    #Vista para eliminar un libro existente
    model = Libro
    template_name = "app_biblioteca/librosDelete.html"
    success_url = reverse_lazy('librosList') #Plantilla para confirmar la eliminación

    def get_object(self):
        nombre = self.kwargs.get("nombre")
        try:
            return Libro.objects.get(nombre=nombre)
        except Libro.DoesNotExist:
            raise Http404("Libro no encontrado")

class RevistaListView(LoginRequiredMixin, ListView): 
    #Vista para mostrar una lista de todos los libros
    model = Revista
    context_object_name="revistas"
    template_name = "app_biblioteca/revistasList.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class RevistaDetailView(LoginRequiredMixin, DetailView):
    #Vista para mostrar los detalles de un libro en particular
    model = Revista
    context_object_name = "revistas"
    template_name = "app_biblioteca/revistasDetail.html"

    def get_object(self):
        return get_object_or_404(Revista, nombre=self.kwargs['nombre'])

class RevistaCreateView(CreateView):
    #Vista para agregar nuevos libros a través de un formulario
    model = Revista
    template_name = "app_biblioteca/RevistasForm.html"
    success_url = reverse_lazy('revistasList') #URL de redireccion después de crear el curso
    fields = ["nombre", "autor", "año"]

class RevistaUpdateView(UpdateView):
    #Vista para actualizar los datos de un libro existente
    model = Revista
    template_name = "app_biblioteca/revistasUpdate.html"
    success_url = reverse_lazy('revistasList')
    fields = ["nombre", "autor","año"]

    def get_object(self):
        nombre = self.kwargs.get("nombre")
        return Revista.objects.get(nombre=nombre)

class RevistaDeleteView(DeleteView):
    #Vista para eliminar un libro existente
    model = Revista
    template_name = "app_biblioteca/revistasDelete.html"
    success_url = reverse_lazy('revistasList') #Plantilla para confirmar la eliminación

    def get_object(self):
        nombre = self.kwargs.get("nombre")
        try:
            return Revista.objects.get(nombre=nombre)
        except Revista.DoesNotExist:
            raise Http404("Revista no encontrada")

class PeliculaListView(LoginRequiredMixin, ListView): 
    #Vista para mostrar una lista de todos los libros
    model = Pelicula
    context_object_name="peliculas"
    template_name = "app_biblioteca/peliculasList.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class PeliculaDetailView(LoginRequiredMixin, DetailView):
    #Vista para mostrar los detalles de un libro en particular
    model = Pelicula
    context_object_name = "peliculas"
    template_name = "app_biblioteca/peliculasDetail.html"

    def get_object(self):
        return get_object_or_404(Pelicula, nombre=self.kwargs['nombre'])

class PeliculaCreateView(CreateView):
    #Vista para agregar nuevos libros a través de un formulario
    model = Pelicula
    template_name = "app_biblioteca/PeliculasForm.html"
    success_url = reverse_lazy('peliculasList') #URL de redireccion después de crear el curso
    fields = ["nombre", "director", "año"]

class PeliculaUpdateView(UpdateView):
    #Vista para actualizar los datos de un libro existente
    model = Pelicula
    template_name = "app_biblioteca/peliculasUpdate.html"
    success_url = reverse_lazy('peliculasList')
    fields = ["nombre", "director","año"]

    def get_object(self):
        nombre = self.kwargs.get("nombre")
        return Pelicula.objects.get(nombre=nombre)

class PeliculaDeleteView(DeleteView):
    #Vista para eliminar un libro existente
    model = Pelicula
    template_name = "app_biblioteca/peliculasDelete.html"
    success_url = reverse_lazy('peliculasList') #Plantilla para confirmar la eliminación

    def get_object(self):
        nombre = self.kwargs.get("nombre")
        try:
            return Pelicula.objects.get(nombre=nombre)
        except Pelicula.DoesNotExist:
            raise Http404("Película no encontrada")
