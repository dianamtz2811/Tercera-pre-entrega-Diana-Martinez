from django.db import models

# Create your models here.
class Libro(models.Model):
    nombre = models.CharField(max_length=40)
    autor = models.CharField(max_length=20)

    def __str__(self):
        return f"Nombre: {self.nombre} - Autor: {self.autor}"

class Revista(models.Model):
    nombre = models.CharField(max_length=40)
    autor = models.CharField(max_length=20)
    año = models.PositiveBigIntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Autor: {self.autor}  - Año: {self.año}"

class Pelicula(models.Model):
    nombre = models.CharField(max_length=40)
    director = models.CharField(max_length=20)
    año = models.PositiveBigIntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Director: {self.director}  - Año: {self.año}"