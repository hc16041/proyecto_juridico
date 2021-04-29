from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

def tipo_de_abogado(request):
    return render(request,'abogados/tipo_de_abogado.html')