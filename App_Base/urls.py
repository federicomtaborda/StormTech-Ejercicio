from django.urls import path
from .views import *

urlpatterns = [
    path('ejercicio/',Ejercicio.as_view(), name='ejercicio'),
    path('resolucion/',Resolucion.as_view(), name='resolucion'),
    path('',Inicio.as_view(), name='index'),
]