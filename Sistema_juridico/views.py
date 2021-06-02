from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView, FormView,View
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
#Decoradores
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
#Autenticacion
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
#Posiblemente este no ira.
from django.contrib.auth.decorators import permission_required
from .forms import *
from .models import *


#Pagina de inicio
class Inicio(LoginRequiredMixin,TemplateView):
    template_name='inicio.html'

#Bloque de vistas para Tipo de Abogados
class ListarTiposDeAbogados(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required='Sistema_juridico.view_tipodeabogado'
    model = TipoDeAbogado
    template_name = "abogados/tp_abogado_listado.html"
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

class CrearTipoDeAbogado(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required='Sistema_juridico.add_tipodeabogado'
    model = TipoDeAbogado
    form_class=TipoDeAbogadoForm
    template_name = "abogados/tp_abogado_crear.html"
    context_object_name='tipos'
    success_url=reverse_lazy('tipo_de_abogado')

class ActualizarTipoDeAbogado(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required='Sistema_juridico.change_tipodeabogado'
    model = TipoDeAbogado
    form_class=TipoDeAbogadoForm
    template_name = "abogados/tp_abogado_editar.html"
    context_object_name='tipos'
    success_url=reverse_lazy('tipo_de_abogado')

class EliminarTipoDeAbogado(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required='Sistema_juridico.delete_tipodeabogado'
    model = TipoDeAbogado
    template_name = "abogados/tp_abogado_borrar.html"
    success_url=reverse_lazy('tipo_de_abogado')

#Bloque de vistas para la sesion
class Login(FormView):
    template_name = 'registration/login.html'
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

def someview(request):
   ...
   return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


#Bloque de vistas para Casos
class ListarCasosClientes(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required='Sistema_juridico.view_caso_cliente'
    model=Caso
    template_name = "casos/caso_list_cliente.html"
    context_object_name='casos'
    paginate_by=10
    
    def get_queryset(self):
        if self.request.user is not None:
            return Caso.objects.filter(
            Q(id_cliente=self.request.user)
        ).distinct()
        return super().get_queryset()

class ListarCasos(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required='Sistema_juridico.view_caso'
    model=Caso
    template_name = "casos/caso_list.html"
    context_object_name='casos'
    paginate_by=10
    queryset=Caso.objects.all()
    
    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return Caso.objects.filter(
            Q(codigo_caso__icontains=self.request.GET['buscar'])|
            Q(estado__icontains=self.request.GET['buscar'])
        ).distinct()
        return super().get_queryset()
    #success_url=reverse_lazy('inicio')

class CrearCaso(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required='Sistema_juridico.add_caso'
    model = Caso, Cliente
    form_class=CasoForm
    template_name = "casos/crear_caso.html"
    success_url=reverse_lazy('caso')

class DetalleCaso(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required='Sistema_juridico.view_caso'
    model = Caso
    template_name = "casos/detalle_caso.html"
    success_url=reverse_lazy('caso')

class ActualizarCaso(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required='Sistema_juridico.change_caso'
    model = Caso
    form_class=CasoForm
    template_name = "casos/caso_editar.html"
    success_url=reverse_lazy('caso')


#Bloque de vistas para Tipo de Procesos
class ListarTiposDeProcesos(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required='Sistema_juridico.view_tipodeproceso'
    model = TipoDeProceso
    template_name = "procesos/tp_proceso_listado.html"
    context_object_name='tp_p'
    queryset=TipoDeProceso.objects.all()
    paginate_by=10
    
    #Para la barra de busqueda
    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return TipoDeProceso.objects.filter(
            Q(nombre__icontains=self.request.GET['buscar'])|
            Q(descripcion__icontains=self.request.GET['buscar'])
        ).distinct()
        return super().get_queryset()

class CrearTipoDeProceso(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required='Sistema_juridico.add_tipodeproceso'
    model = TipoDeProceso
    form_class=TipoDeProcesoForm
    template_name = "procesos/tp_proceso_crear.html"
    context_object_name='tipos'
    success_url=reverse_lazy('tipo_de_proceso')

class ActualizarTipoDeProceso(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required='Sistema_juridico.change_tipodeproceso'
    model = TipoDeProceso
    form_class=TipoDeProcesoForm
    template_name = "procesos/tp_proceso_editar.html"
    context_object_name='tipos'
    success_url=reverse_lazy('tipo_de_proceso')

class EliminarTipoDeProceso(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required='Sistema_juridico.delete_tipodeproceso'
    model = TipoDeProceso
    template_name = "abogados/tp_abogado_borrar.html"
    success_url=reverse_lazy('tipo_de_proceso')


#Bloque de vistas para Abogado
class ListarAbogado(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required='Sistema_juridico.view_abogado'
    model=Abogado
    template_name = "abogados/abogado_list.html"
    context_object_name='abogados'
    paginate_by=10
    queryset=Abogado.objects.all()
    
    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return Abogado.objects.filter(
            Q(nombre__icontains=self.request.GET['buscar'])|
            Q(correo__icontains=self.request.GET['buscar'])|
            Q(dui__icontains=self.request.GET['buscar'])
        ).distinct()
        return super().get_queryset()
    #success_url=reverse_lazy('inicio')

class CrearAbogado(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    permission_required='Sistema_juridico.add_abogado'
    model = Abogado
    form_class=FormAbogado
    template_name = "abogados/crear_abogado.html"
    context_object_name='abogados'
    success_url=reverse_lazy('abogados')

class ActualizarAbogado(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required='Sistema_juridico.change_abogado'
    model = Abogado
    form_class= FormAbogado
    template_name = "abogados/editar_abogado.html"
    success_url=reverse_lazy('abogados')   

class DetalleAbogado(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required='Sistema_juridico.view_abogado'
    model = Abogado
    template_name = "abogados/detalle_abogado.html"
    success_url = reverse_lazy('abogados')

#Bloque de vistas para Cliente
class ListaCliente(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required='Sistema_juridico.view_cliente'
    model=Cliente
    template_name = "clientes/cliente_list.html"
    context_object_name='clientes'
    #solo los que son cliente
    queryset=Cliente.objects.all()
    paginate_by=10
    
    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return Cliente.objects.filter(
            Q(nombre__icontains=self.request.GET['buscar'])|
            Q(correo__icontains=self.request.GET['buscar'])|
            Q(dui__icontains=self.request.GET['buscar'])
        ).distinct()
        return super().get_queryset()

class CrearCliente(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required='Sistema_juridico.add_cliente'
    model = Cliente, Rol
    form_class=FormCliente
    template_name = "clientes/cliente_crear.html"
    context_object_name='tipos'
    success_url=reverse_lazy('cliente')

class ActualizarCliente(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required='Sistema_juridico.change_cliente'
    model = Cliente
    form_class=FormCliente
    template_name = "clientes/cliente_editar.html"
    success_url=reverse_lazy('cliente')

class DetalleCliente(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required='Sistema_juridico.view_cliente'
    model = Cliente
    template_name = "clientes/detalle_cliente.html"
    success_url=reverse_lazy('clientes')


#Bloque de vistas para Institucion
class ListarInstitucion(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required='Sistema_juridico.view_institucion'
    model = Institucion
    template_name = "institucion/institucion_list.html"
    context_object_name='institucion'
    queryset=Institucion.objects.all()
    paginate_by=2
    
    #Para la barra de busqueda
    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return Institucion.objects.filter(
            Q(nombre__icontains=self.request.GET['buscar'])|
            Q(direccion__icontains=self.request.GET['buscar'])
        ).distinct()
        return super().get_queryset()

class CrearInstitucion(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required='Sistema_juridico.add_institucion'
    model = Institucion
    form_class= InstitucionForm
    template_name = "institucion/crear_institucion.html"
    context_object_name='institucion'
    success_url=reverse_lazy('institucion')

class EliminarInstitucion(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required='Sistema_juridico.delete_institucion'
    model = Institucion
    template_name = "institucion/borrar_institucion.html"
    success_url=reverse_lazy('institucion')

class ActualizarInstitucion(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required='Sistema_juridico.change_institucion'
    model = Institucion
    form_class=InstitucionForm
    template_name = "institucion/editar_institucion.html"
    context_object_name='institucion'
    success_url=reverse_lazy('institucion')

#Bloque de vistas para Audiencia
class ListaAudiencia(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required='Sistema_juridico.view_audiencia'
    model = Audiencia, Caso
    template_name = "audiencia/audiencia_list.html"
    context_object_name='audiencia'
    queryset=Audiencia.objects.all()
    paginate_by=10
    
    #Para la barra de busqueda

    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return Audiencia.objects.filter(
            Q(detalle__icontains=self.request.GET['buscar'])|
            Q(codigo_caso_id=self.request.GET['buscar'])|
            Q(descripcion__icontains=self.request.GET['buscar'])
        ).distinct()
        return super().get_queryset()

class CrearAudiencia(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required='Sistema_juridico.add_audiencia'
    model = Audiencia
    form_class= AudienciaForm
    template_name = "audiencia/crear_audiencia.html"
    context_object_name='audiencia'
    success_url=reverse_lazy('audiencia')

class ActualizarAudiencia(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required='Sistema_juridico.change_audiencia'
    model = Audiencia
    form_class=AudienciaForm
    template_name = "audiencia/audiencia_editar.html"
    context_object_name='audiencia'
    success_url=reverse_lazy('audiencia')

#Bloque de vistas para Pagos
class ListarPagos(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required='Sistema_juridico.view_pago'
    model = Pago
    template_name = "pagos/pago_list.html"
    context_object_name='pagos'
    queryset=Pago.objects.order_by('fecha')
    paginate_by=10
    
    #Para la barra de busqueda

    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return Pago.objects.filter(
            Q(codigo_caso_id=self.request.GET['buscar'])
        ).distinct()
        return super().get_queryset()

class CrearPago(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required='Sistema_juridico.add_pago'
    model = Pago, Caso
    form_class= PagoForm
    template_name = "pagos/crear_pago.html"
    context_object_name='pagos'
    success_url=reverse_lazy('pagos')

class AbonarPago(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required={'Sistema_juridico.add_pago','Sistema_juridico.change_pago','Sistema_juridico.change_pago'}
    model = Pago, Caso
    form_class= PagoForm
    template_name = "pagos/crear_pagos.html"
    context_object_name='pagos'
    success_url=reverse_lazy('pagos')

class ActualizarPago(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required='Sistema_juridico.change_pago'
    model = Pago
    form_class= PagoForm
    template_name = "pagos/editar_pago.html"
    success_url=reverse_lazy('pagos') 


#Bloque de vistas para Errores
def handler403(request,exception=None):
    return render(request,'errores/403.html')

def handler404(request,exception=None):
    return render(request,'errores/404.html')