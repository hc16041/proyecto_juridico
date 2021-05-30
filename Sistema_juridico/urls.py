from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),
    #Urls para Tipo de Abogado
    path('tipo_de_abogado/',ListarTiposDeAbogados.as_view(), name='tipo_de_abogado'),
    path('crear_tipo_de_abogado/',CrearTipoDeAbogado.as_view(),name='crear_tipo_de_abogado'),
    path('editar_tipo_de_abogado/<int:pk>',ActualizarTipoDeAbogado.as_view(),name='editar_tipo_de_abogado'),
    path('eliminar_tipo_de_abogado/<int:pk>/',EliminarTipoDeAbogado.as_view(),name='eliminar_tipo_de_abogado'),
    
    #Urls para Casos
    path('caso/',ListarCasos.as_view(), name='caso'),
    path('caso_cliente/',ListarCasosClientes.as_view(),name='caso_cliente'),
    path('crear_caso/',CrearCaso.as_view(),name='crear_caso'),
    path('editar_caso/<pk>', ActualizarCaso.as_view(), name='editar_caso'),
    path('detalle_caso/<pk>', DetalleCaso.as_view(), name='detalle_caso'),
    
    #Urls para Tipo de Procesos
    path('tipo_de_proceso/',ListarTiposDeProcesos.as_view(), name='tipo_de_proceso'),
    path('crear_tipo_de_proceso/',CrearTipoDeProceso.as_view(),name='crear_tipo_de_proceso'),
    path('editar_tipo_de_proceso/<int:pk>',ActualizarTipoDeProceso.as_view(),name='editar_tipo_de_proceso'),
    path('eliminar_tipo_de_proceso/<int:pk>/',EliminarTipoDeProceso.as_view(),name='eliminar_tipo_de_proceso'),
    
    #Urls para Institucion
    path('institucion/', ListarInstitucion.as_view(), name='institucion'),
    path('crear_institucion/', CrearInstitucion.as_view(), name='crear_institucion'),
    path('editar_institucion/<int:pk>', ActualizarInstitucion.as_view(), name='editar_institucion'),
    path('eliminar_institucion/<int:pk>/', EliminarInstitucion.as_view(), name='eliminar_institucion'),
    
    #Urls para Abogados
    path('abogados/',ListarAbogado.as_view(), name='abogados'),
    path('crear_abogado/',CrearAbogado.as_view(),name='crear_abogado'),
    path('editar_abogado/<int:pk>',ActualizarAbogado.as_view(),name='editar_abogado'),
    path('detalle_abogado/<int:pk>', DetalleAbogado.as_view(), name='detalle_abogado'),
    
    #Urls para Clientes
    path('cliente/', ListaCliente.as_view(), name='cliente'),
    path('crear_cliente/',CrearCliente.as_view(),name='crear_cliente'),
    path('editar_cliente/<int:pk>',ActualizarCliente.as_view(),name='editar_cliente'),
    path('detalle_cliente/<int:pk>', DetalleCliente.as_view(), name='detalle_cliente'),

    #Urls para Pagos
    path('crear_pago', CrearPago.as_view(), name='crear_pago'),
    path('pagos/', ListarPagos.as_view(), name= 'pagos'),
    path('abonar_pago/<id>', AbonarPago.as_view(), name= 'abonar_pago'),
    path('editar_pago/<pk>', ActualizarPago.as_view(), name = 'editar_pago'),
    
    #Urls para Audiencias
    path('audiencia/', ListaAudiencia.as_view(), name= 'audiencia'),
    path('crear_audiencia/', CrearAudiencia.as_view(), name='crear_audiencia'),
    path('editar_audiencia/<int:pk>', ActualizarAudiencia.as_view(), name='editar_audiencia'),
    
    #Urls para errores personalizados
    path('403/', handler403),
    path('404/', handler404),
]
