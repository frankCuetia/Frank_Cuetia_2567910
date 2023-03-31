from django.db import models
from django.db.models.fields import *

class Auto(models.Model):
  marca = CharField(max_length=20)
  nombre = CharField(max_length=30)
  modelo = IntegerField()
  color = CharField(max_length=20)

  def __str__(self):
    return self.nombre

class Cliente(models.Model):
  nombre = CharField(max_length=20)
  apellido = CharField(max_length=30)
  direccion = CharField(max_length=200)
  email = EmailField(max_length=100)
  telefono = CharField(max_length=20)

  def __str__(self):
    return self.nombre
  

