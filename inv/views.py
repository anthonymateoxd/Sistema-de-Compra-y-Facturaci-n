from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Categoria
from django.http import HttpResponse

class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

def Home(request):
    return HttpResponse("¡Hola desde la aplicación inv!")
