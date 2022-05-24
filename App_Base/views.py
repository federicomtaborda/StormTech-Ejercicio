from django.shortcuts import render
from django.views import generic

# Create your views here.

class Inicio(generic.TemplateView):
    template_name = 'App_Base/index.html'

class Ejercicio(generic.TemplateView):
    template_name = 'App_Base/ejercicio.html'

class Resolucion(generic.TemplateView):
    template_name = 'App_Base/resolucion.html'