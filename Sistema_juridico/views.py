from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .forms import TipoDeAbogadoForm, FormLogin, CasoForm, TipoDeProcesoForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView, FormView
from django.db.models import Q
from .models import  TipoDeAbogado, Caso, TipoDeProceso
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# Create your views here.
class Inicio(TemplateView, LoginRequiredMixin):
    template_name='inicio.html'
    
class ListarTiposDeAbogados(ListView):
    model = TipoDeAbogado
    template_name = "abogados/tipo_de_abogado_list.html"
    context_object_name='tipos'
    queryset=TipoDeAbogado.objects.all()
    paginate_by=10
    
    #Para la barra de busqueda
    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return TipoDeAbogado.objects.filter(
            Q(nombre__icontains=self.request.GET['buscar'])|
            Q(descripcion__icontains=self.request.GET['buscar'])
        ).distinct()
        return super().get_queryset()
    
class CrearTipoDeAbogado(CreateView):
    model = TipoDeAbogado
    form_class=TipoDeAbogadoForm
    template_name = "abogados/crear_tipo_de_abogado.html"
    context_object_name='tipos'
    success_url=reverse_lazy('tipo_de_abogado')
    
class ActualizarTipoDeAbogado(UpdateView):
    model = TipoDeAbogado
    form_class=TipoDeAbogadoForm
    template_name = "abogados/editar_tipo_de_abogado.html"
    context_object_name='tipos'
    success_url=reverse_lazy('tipo_de_abogado')
    
class EliminarTipoDeAbogado(DeleteView):
    model = TipoDeAbogado
    template_name = "abogados/tipo_de_abogado_confirm_delete.html"
    success_url=reverse_lazy('tipo_de_abogado')
    

class Login(FormView):
    template_name = 'sesion/login.html'
    form_class = FormLogin
    context_object_name='login'
    success_url = reverse_lazy('inicio')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/sesion/login/')

from django.http import HttpResponseRedirect

def someview(request):
   ...
   return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class CrearCaso(CreateView):
    model = Caso
    form_class=CasoForm
    template_name = "casos/caso.html"
    success_url=reverse_lazy('inicio')

class CrearTipoDeProceso(CreateView):
    model =TipoDeProceso
    form_class=TipoDeProcesoForm
    template_name = "procesos/crear_tipo_proceso.html"
    success_url=reverse_lazy('tipo_de_abogado')
    