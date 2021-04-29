from django.urls import path
from .views import inicio, tipo_de_abogado

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('tipo_de_abogado/',tipo_de_abogado, name='tipo_de_abogado')
]
