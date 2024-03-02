from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from navegadoresWebs.models import Navegador

class navegadores(ListView):
    model = Navegador
    context_object_name = "listado_navegadores"
    template_name = "navegadores/navegadores.html"

  
class CreacionNavegadores(LoginRequiredMixin,CreateView):
    model = Navegador
    template_name = "navegadores/creacionNavegadores.html"
    fields = ["nombre", "version", "fecha_creacion"]
    success_url = reverse_lazy("navegadores")


class ActualizarNavegadores(LoginRequiredMixin,UpdateView):
    model = Navegador
    template_name = "navegadores/actualizarNavegadores.html"
    fields = ["nombre", "version", "fecha_creacion"]
    success_url = reverse_lazy("navegadores")

class DetalleNavegador(DetailView):
    model = Navegador
    template_name = "navegadores/detalleNavegadores.html"


class EliminarNavegador(LoginRequiredMixin,DeleteView):
    model = Navegador
    template_name = "navegadores/eliminarNavegadores.html"
    success_url = reverse_lazy("navegadores")
