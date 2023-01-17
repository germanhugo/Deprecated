from django.db import models

# Create your models here.

class Automovil(models.Model):

    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    patente = models.CharField(max_length=7)

class Service(models.Model):

    fecha = models.DateField()
    cambioAceite = models.BooleanField()
    cambioFiltros = models.BooleanField()
    valor = models.FloatField()

class Cliente(models.Model):

    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=11)


