from django.urls import path
from .views import *

urlpatterns = [
    path('',principal,name='principal'),
    path('clientes/',clientes,name='clientes'),
    path('autos/',autos,name='autos'),
]

