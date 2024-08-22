from django.db import models

# Create your models here.
class Libro(models.Model):
    nombre = models.CharField(max_length=40)
    autor = models.CharField(max_length=20)

class Revista(models.Model):
    nombre = models.CharField(max_length=40)
    autor = models.CharField(max_length=20)
    año = models.PositiveBigIntegerField()

class Pelicula(models.Model):
    nombre = models.CharField(max_length=40)
    director = models.CharField(max_length=20)
    año = models.PositiveBigIntegerField()