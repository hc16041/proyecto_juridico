from django.shortcuts import render, render_to_response
from django.urls import reverse, reverse_lazy
from .forms import *
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView, FormView,View
from django.db.models import Q
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from .mixins import LoginYSuperStaffMixin,LoginMixin,ValidarPermisosMixin
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.template import RequestContext


# Create your views here.

class Inicio(LoginRequiredMixin,TemplateView):
    template_name='inicio.html'

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

def someview(request):
   ...
   return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class CrearCaso(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required='Sistema_juridico.add_caso'
    model = Caso
    form_class=CasoForm
    template_name = "casos/caso.html"
    success_url=reverse_lazy('inicio')


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
    permission_required='Sistema_juridico.change_caso'
    model = TipoDeProceso
    form_class=TipoDeProcesoForm
    template_name = "procesos/tp_proceso_editar.html"
    context_object_name='tipos'
    success_url=reverse_lazy('tipo_de_proceso')

class EliminarTipoDeProceso(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required='Sistema_juridico.delete_caso'
    model = TipoDeProceso
    template_name = "abogados/tp_abogado_borrar.html"
    success_url=reverse_lazy('tipo_de_proceso')

class ListaAbogado(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required='Sistema_juridico.view_abogado'
    model=Abogado
    template_name = "abogados/abogado_list.html"
    context_object_name='abogados'
    #solo los que son abogado
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
    permission_required=('Sistema_juridico.view_abogado','Sistema_juridico.add_abogado')
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
    #success_url=reverse_lazy('inicio')

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

class EliminarCliente(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required='Sistema_juridico.delete_cliente'
    model = Cliente
    template_name = "clientes/cliente_borrar.html"
    success_url=reverse_lazy('cliente')

class DetalleCliente(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required='Sistema_juridico.view_cliente'
    model = Cliente
    template_name = "clientes/detalle_cliente.html"
    success_url=reverse_lazy('clientes')

class ListaCasos(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required='Sistema_juridico.view_caso'
    model=Caso
    template_name = "casos/listar.html"
    context_object_name='clientes'
    #solo los que son cliente
    queryset=Caso.objects.all()
    
    def get_login_url(self):
        if not self.request.user.is_authenticated:
            # el usuario no está logueado, ir a la página de login
            return super(ListaCasos, self).get_login_url()
        # El usuario está logueado pero no está autorizado
        return '/no_autorizado/'
    
    def test_func(self):
        # obtenemos todos los grupos del usuario logueado
        grupos = self.request.user.groups.all()
        # comparamos que el usuario pertenezca al grupo GERENTE
        if 'Abogado' in grupos:
            return True
        return False
    
    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return Caso.objects.filter(
            Q(nombre__icontains=self.request.GET['buscar'])|
            Q(correo__icontains=self.request.GET['buscar'])|
            Q(dui__icontains=self.request.GET['buscar'])
        ).distinct()
        return super().get_queryset()
    #success_url=reverse_lazy('inicio')

class ListaReportes(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required='Sistema_juridico.view_reporte'
    model=Reporte
    template_name = "reportes/reporte_list.html"
    context_object_name='reportes'
    queryset=Reporte.objects.all()
    paginate_by=10
    
    #Para la barra de busqueda
    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return Reporte.objects.filter(
            Q(nombre__icontains=self.request.GET['buscar'])|
            Q(descripcion__icontains=self.request.GET['buscar'])
        ).distinct()
        return super().get_queryset()

class contactomail(LoginRequiredMixin,View):
    def get(self,request):
        form=contactoForm()
        return render(request,'email.html',{'forma':form})
    def post(self,request):
        form=contactoForm(request.POST)
        if form.is_valid():
            datos=form.cleaned_data

            email = send_mail('title', 'body', to=['Jennifereunicemonge@gmail.com'])
            email.send()

            return HttpResponseRedirect('/')
        return render(request,'email.html',{'forma':form})

class ListarInstitucion(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required='Sistema_juridico.view_institucion'
    model = Institucion
    template_name = "instituciones/institucion_list.html"
    context_object_name='institucion'
    queryset=Institucion.objects.all()
    paginate_by=10
    
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
    template_name = "instituciones/crear_institucion.html"
    context_object_name='institucion'
    success_url=reverse_lazy('institucion')

class EliminarInstitucion(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required='Sistema_juridico.delete_institucion'
    model = Institucion
    template_name = "instituciones/institucion_confirm_delete.html"
    success_url=reverse_lazy('institucion')

class ActualizarInstitucion(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required='Sistema_juridico.change_institucion'
    model = Institucion
    form_class=InstitucionForm
    template_name = "instituciones/editar_institucion.html"
    context_object_name='institucion'
    success_url=reverse_lazy('institucion')

def handler403(request,exception=None):
    return render(request,'errores/403.html')

def handler404(request,exception=None):
    return render(request,'errores/404.html')


