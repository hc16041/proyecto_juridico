from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import FormUsuario
from .models import *
# Register your models here.


 
admin.site.register(Usuario)
admin.site.register(TipoDeAbogado)
admin.site.register(Caso)
admin.site.register(Pago)
admin.site.register(Abogado)
admin.site.register(TipoDeProceso)
admin.site.register(FormaDePago)
admin.site.register(Audiencia)
admin.site.register(Cliente)
admin.site.register(USCitizen)

