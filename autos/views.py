from django.shortcuts import render
from .models import *

def principal(request):
  return render(request,'principal.html')

def autos(request):
  datos = {
    'autos':Auto.objects.all()
  }
  return render(request,'autos.html',datos)

def clientes(request):
  datos = {
    'clientes':Cliente.objects.all()
  }
  return render(request,'clientes.html',datos)
