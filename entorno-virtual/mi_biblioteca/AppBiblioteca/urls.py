from AppBiblioteca import views
from django.urls import path

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('libros/', views.libros, name='libros'),
    path('revistas/', views.revistas, name='revistas'),
    path('peliculas/', views.peliculas, name='peliculas'),
    path('libroFormulario/', views.libro_Formulario, name='libroFormulario'),
    path('revistaFormulario/', views.revista_Formulario, name='revistaFormulario'),
    path('peliculaFormulario/', views.pelicula_Formulario, name='peliculaFormulario'),
    path('busquedaDirector/', views.busqueda_Director, name='busquedaDirector'),
    path('buscar/', views.buscar, name='buscar'),
]