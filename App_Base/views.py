from urllib import request
from django.shortcuts import render, get_list_or_404
from django.views import View, generic

from .forms import PantillaFrom
from .models import Plantilla

# Create your views here.

class Inicio(View):
  def get(self, request, *args, **kwargs):
      num_plantillas = Plantilla.objects.all()
      context={
          'plantillas':num_plantillas
        }
      return render(request,'App_Base/index.html',context)

  ### METODO POST ###
  def post(self, request, *args, **kwargs):
    form = PantillaFrom(request.POST)
    if request.method=="POST":
      context={
          'fom':form
        }
      return render(request,'App_Base/index.html')


class Ejercicio(generic.TemplateView):
    template_name = 'App_Base/ejercicio.html'

class Resolucion(generic.TemplateView):
    template_name = 'App_Base/resolucion.html'
