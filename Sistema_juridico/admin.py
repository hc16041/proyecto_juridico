from django.contrib import admin
from .models import TipoDeAbogado
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import FormUsuario
from .models import Usuario
# Register your models here.


# class UserAdmin(BaseUserAdmin):
#     form=FormActualizarUsuario
#     add_form=FormAdminCrearUsuario
    
#     list_display=('correo','admin')
#     list_filter=('admin',)
#     fieldsets = (
#         (None, {
#             "fields": (
#                 'correo','password'
#             ),
#         }),
#         ('Información Personal',{'fields':('nombre','apellido',)}),
#         ('Permisos Django',{'fields':('admin','staff')}),
#     )
#     add_fieldsets=(
#         (None,{
#             'classes':('wide',),
#             'fields':('correo','password1','password2')
#         }),
#     )
    
#     search_fields=('correo',)
#     ordering=('correo',)
#     filter_horizontal=()
    
#admin.site.register(Usuario,UserAdmin)
admin.site.register(TipoDeAbogado)
admin.site.register(Usuario)
