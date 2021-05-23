from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),

    path('tipo_de_abogado/',login_required(ListarTiposDeAbogados.as_view()), name='tipo_de_abogado'),
    path('crear_tipo_de_abogado/',CrearTipoDeAbogado.as_view(),name='crear_tipo_de_abogado'),
    path('editar_tipo_de_abogado/<int:pk>',ActualizarTipoDeAbogado.as_view(),name='editar_tipo_de_abogado'),
    
    path('tipo_de_proceso/',login_required(ListarTiposDeProcesos.as_view()), name='tipo_de_proceso'),
    path('crear_tipo_de_proceso/',CrearTipoDeProceso.as_view(),name='crear_tipo_de_proceso'),
    path('editar_tipo_de_proceso/<int:pk>',ActualizarTipoDeProceso.as_view(),name='editar_tipo_de_proceso'),
    path('eliminar_tipo_de_proceso/<int:pk>/',EliminarTipoDeProceso.as_view(),name='eliminar_tipo_de_proceso'),

    path('cliente/',ListaCliente.as_view(), name='cliente'),
    path('crear_cliente/',CrearCliente.as_view(),name='crear_cliente'),
    path('editar_cliente/<int:pk>',ActualizarCliente.as_view(),name='editar_cliente'),
    path('eliminar_cliente/<int:pk>',EliminarCliente.as_view(),name='eliminar_cliente'),

    path('institucion/', login_required(ListarInstitucion.as_view()), name='institucion'),
    path('crear_institucion/', CrearInstitucion.as_view(), name='crear_institucion'),
    path('editar_institucion/<int:pk>', ActualizarInstitucion.as_view(), name='editar_institucion'),
    path('eliminar_institucion/<int:pk>/', EliminarInstitucion.as_view(), name='eliminar_institucion'),

    path('abogados/', login_required(ListarAbogado.as_view()), name='abogado'),
    path('crear_abogado/', CrearAbogado.as_view(), name='crear_abogado'),
    path('editar_abogado/<int:pk>', ActualizarAbogado.as_view(), name='editar_abogado'),
    path('eliminar_abogado/<int:pk>/', EliminarAbogado.as_view(), name='eliminar_abogado'),

    path('crear_caso/',CrearCaso.as_view(),name='crear_caso'),
]
