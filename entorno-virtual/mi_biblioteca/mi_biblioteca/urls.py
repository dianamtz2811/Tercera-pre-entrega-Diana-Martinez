"""
URL configuration for mi_biblioteca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from mi_biblioteca.views import agregar_libro, agregar_revista, agregar_pelicula

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppBiblioteca/', include('AppBiblioteca.urls')),
    path('users/', include ('users.urls')),
    path('agregar_libro/<nom>/<aut>/', agregar_libro),
    path('agregar_revista/<nom>/<aut>/<año>/', agregar_revista),
    path('agregar_pelicula/<nom>/<dir>/<año>/', agregar_pelicula)

]
