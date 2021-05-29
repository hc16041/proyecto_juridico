from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),
    path('tipo_de_abogado/',ListarTiposDeAbogados.as_view(), name='tipo_de_abogado'),
    path('crear_tipo_de_abogado/',CrearTipoDeAbogado.as_view(),name='crear_tipo_de_abogado'),
    path('editar_tipo_de_abogado/<int:pk>',ActualizarTipoDeAbogado.as_view(),name='editar_tipo_de_abogado'),
    path('eliminar_tipo_de_abogado/<int:pk>/',EliminarTipoDeAbogado.as_view(),name='eliminar_tipo_de_abogado'),

<<<<<<< HEAD
    path('crear_caso/',CrearCaso.as_view(),name='crear_caso'),

    path('tipo_de_proceso/',ListarTiposDeProcesos.as_view(), name='tipo_de_proceso'),
=======
    path('tipo_de_proceso/',login_required(ListarTiposDeProcesos.as_view()), name='tipo_de_proceso'),
>>>>>>> e06f98875dfd7f4424424f9eb4e0543009413e2b
    path('crear_tipo_de_proceso/',CrearTipoDeProceso.as_view(),name='crear_tipo_de_proceso'),
    path('editar_tipo_de_proceso/<int:pk>',ActualizarTipoDeProceso.as_view(),name='editar_tipo_de_proceso'),
    path('eliminar_tipo_de_proceso/<int:pk>/',EliminarTipoDeProceso.as_view(),name='eliminar_tipo_de_proceso'),

    path('institucion/', ListarInstitucion.as_view(), name='institucion'),
    path('crear_institucion/', CrearInstitucion.as_view(), name='crear_institucion'),
    path('editar_institucion/<int:pk>', ActualizarInstitucion.as_view(), name='editar_institucion'),
    path('eliminar_institucion/<int:pk>/', EliminarInstitucion.as_view(), name='eliminar_institucion'),

    path('abogados/',ListaAbogado.as_view(), name='abogados'),
    path('crear_abogado/',CrearAbogado.as_view(),name='crear_abogado'),
    path('editar_abogado/<int:pk>',ActualizarAbogado.as_view(),name='editar_abogado'),
    path('detalle_abogado/<int:pk>', DetalleAbogado.as_view(), name='detalle_abogado'),

    path('cliente/', ListaCliente.as_view(), name='cliente'),
    path('crear_cliente/',CrearCliente.as_view(),name='crear_cliente'),
    path('editar_cliente/<int:pk>',ActualizarCliente.as_view(),name='editar_cliente'),
    path('detalle_cliente/<int:pk>', DetalleCliente.as_view(), name='detalle_cliente'),

    path('crear_caso/',login_required(CrearCaso.as_view()),name='crear_caso'),
    path('caso/',ListaCasos.as_view(), name='caso'),
<<<<<<< HEAD
    path('reporte/',ListaReportes.as_view(),name='reporte'),
    path('403/', handler403),
    path('404/', handler404),

=======
    path('detalle_caso/<int:pk>',DetalleCaso.as_view(),name='detalle_caso'),
    path('editar_caso/<int:pk>',ActualizarCaso.as_view(),name='editar_caso'),
    path('asignar_cliente/',AsignarCliente.as_view(),name='asignar_cliente'),

    path('formaPago_crear/',CrearFormaDePagoModal.as_view(),name='formaPago_crear'),
    path('crear_formaPago/',CrearFormaDePago.as_view(),name='crear_formaPago'),
    path('formaPago/',login_required(ListaFormaDePago.as_view()), name='formaPago'),
    path('eliminar_formaPago/<int:pk>',EliminarFormaDePago.as_view(),name='eliminar_formaPago'),
    path('editar_formaPago/<int:pk>',ActualizarFormaDePago.as_view(),name='editar_formaPago'),

    path('crear_audiencia/',CrearAudiencia.as_view(),name='crear_audiencia'),
    path('audiencia/',login_required(ListaAudiencia.as_view()), name='audiencia'),
    path('editar_audiencia/<int:pk>',ActualizarAudiencia.as_view(),name='editar_audiencia'),
    path('eliminar_audiencia/<int:pk>',EliminarAudiencia.as_view(),name='eliminar_audiencia'),
    
>>>>>>> e06f98875dfd7f4424424f9eb4e0543009413e2b
]
