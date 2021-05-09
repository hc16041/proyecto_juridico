from django.urls import path
from .views import ListarTiposDeAbogados, Inicio, CrearTipoDeAbogado, ActualizarTipoDeAbogado, EliminarTipoDeAbogado, CrearCaso,CrearTipoDeProceso
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),
    path('tipo_de_abogado/',login_required(ListarTiposDeAbogados.as_view()), name='tipo_de_abogado'),
    path('crear_tipo_de_abogado/',CrearTipoDeAbogado.as_view(),name='crear_tipo_de_abogado'),
    path('editar_tipo_de_abogado/<int:pk>',ActualizarTipoDeAbogado.as_view(),name='editar_tipo_de_abogado'),
    path('eliminar_tipo_de_abogado/<int:pk>/',EliminarTipoDeAbogado.as_view(),name='eliminar_tipo_de_abogado'),
    path('crear_caso/',CrearCaso.as_view(),name='crear_caso'),
    path('crear_tipo_de_proceso/',CrearTipoDeProceso.as_view(),name='crear_tipo_de_proceso'),
]
