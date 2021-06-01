from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import Permission, User #Usuario
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from proyecto_juridico import settings


class TipoDeAbogadoForm(forms.ModelForm):
    class Meta:
        model=TipoDeAbogado
        fields='__all__'
        labels={
            'nombre': 'Nombre del tipo',
            'descripcion':'Descripcion'
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del tipo de abogado',
                    'id':'nombre',
                    
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese descripcion del tipo de abogado',
                    'rows': '3',
                    'id':'descripcion',
                }
            ),
        }
    
class TipoDeProcesoForm(forms.ModelForm):
    class Meta:
        model=TipoDeProceso
        fields='__all__'
        labels={
            'nombre': 'Nombre del tipo',
            'descripcion':'Descripcion'
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del tipo de proceso',
                    'id':'nombre',
                    
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':'3',
                    'placeholder':'Ingrese descripcion del tipo de proceso',
                    'rows': '3',
                    'id':'descripcion',
                }
            ),
        }

class FormLogin(AuthenticationForm):
    class Meta:
        db_table = Usuario
        fields=['correo','password']
        labels={
            'username': 'Nombre del tipo',
            'password':'Contraseña'
        }
    
        widgets={
            'correo': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el correo ',
                    'id':'correo'
                }
            ),
            'password':forms.PasswordInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese contraseña',
                    'id':'password',
                }
            ),
        }
    
class CasoForm(forms.ModelForm):
    codigo_caso=forms.IntegerField(min_value=1,max_value=1500000)
    class Meta:
        model=Caso
        fields='__all__'
        labels={
            'codigo caso': 'Codigo caso',
            'descripcion':'Descripcion'
        }
        widgets={
            'id_cliente': forms.Select(
                attrs={
                    'id':'id_cliente',
                    'class':'form-control form-control-sm col-sm-6',
                }
            ),
            'id_abogado': forms.Select(
                attrs={
                    'id':'id_abogado',
                    'class':'form-control form-control-sm col-sm-6',
                }
            ),
            'codigo': forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm col-sm-6',
                    'placeholder':'Ingrese el codigo del caso',
                    'id':'codigo',
                    
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm col-sm-6',
                    'placeholder':'Ingrese descripcion del tipo de abogado',
                    'id':'descripcion',
                }
            ),
            'estado':forms.Select(
                attrs={
                    'id':'estado',
                    'class':'form-control form-control-sm col-sm-6'
                }
            ),
            'tipo_de_proceso':forms.Select(
                attrs={
                    'id':'tipo_de_proceso',
                    'class':'form-control form-control-sm col-sm-6'
                }
            ),
            'tipo_pago':forms.RadioSelect(
                attrs={
                    '':'Contado',
                    '':'Credito',
                    'id':'tipo_pago',
                }
            ),
            
        }
    
class AudienciaForm(forms.ModelForm):
    class Meta:
        model=Audiencia
        fields= '__all__'
        labels={
        }
        widgets={
            'codigo_caso':forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'--',
                    'id':'codigo_caso',
                }
            ),
            'id_cliente':forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'-- ',
                    'id':'id_cliente',
                }
            ),
           'detalle':forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'--',
                    'id':'detalle',
                }
            ),
           'fecha':forms.SelectDateWidget(
                     years=range(2021, 2100),
                     attrs={
                         'class':'form-control form-control-sm col-sm-2',
                         'type': 'date',
                         'id':'fecha',
                         }
                 ),   
           'hora':forms.TimeInput(
                attrs={
                    'type': 'time',
                    'id':'hora',
                    'class':'form-control',
                }
            ),
           'juzgado':forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'---',
                    'id':'juzgado',
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows' : '4',
                    'placeholder':'Descripcion de audiencia',
                    'id':'descripcion'
                         }
                 ),
        }

class PagoForm(forms.ModelForm):
    class Meta:
        model=Pago
        fields='__all__'
        labels={
        }
        widgets={
           'fecha':forms.SelectDateWidget(
                     years=range(2021, 2100),
                     attrs={
                         'class':'form-control form-control-sm col-sm-2',
                         'type': 'date',
                         'id':'fecha_pago',
                         }
                 ),
            'descripcion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese descripcion sobre el abono realizado',
                    'rows': '2',
                    'id':'descripcion',
                        }
                ),
            'monto':forms.TextInput(
                     attrs={
                         'class':'form-control form-control-sm col-sm-4',
                         'id':'monto'
                         }
                 ),
        }

class FormCliente(forms.ModelForm):
    
    class Meta:
        model=Cliente
        fields=('nombre','apellido','dui','direccion','correo','telefono','estado_civil','fecha_nacimiento')
        widgets={
                 'nombre': forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese el nombre del cliente',
                         'id':'nombre',
                     }
            ),
                 'correo':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese correo del cliente',
                         'id':'correo',
                     }
            ),
                 'apellido':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese apellido del cliente',
                         'id':'apellido',
                     }
                 ),
                 'direccion':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese la direccion del cliente',
                         'id':'direccion',
                     }),
                 'telefono':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese telefono del cliente',
                         'id':'telefono',
                     }
            ),
                 'dui': forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder': 'Ingrese numero de dui',
                         'id':'dui',
                     }
            ),
                 'estado_civil':forms.Select(
                attrs={
                    'id':'estado_civil',
                    'class':'form-control form-control-sm col-sm-2'
                }
            ),
                 'fecha_nacimiento':forms.SelectDateWidget(
                     years=range(1900, 2020),
                     attrs={
                         'class':'form-control form-control-sm col-sm-2',
                         'type': 'date',
                         'id':'fecha_nacimiento',
                         }
                 )   
             }

    def save(self,commit=True):
        #creacion de contraseña aleatoriamente
        password1=BaseUserManager().make_random_password(15)
        nombre=self.cleaned_data.get("nombre")
        apellido=self.cleaned_data.get("apellido")
        correo=self.cleaned_data.get("correo")
        usuario=super().save(commit=False)
        
        #se agrega el rol de una vez
        usuario.rol=Rol.objects.get(id=1)
        
        #Se crea un usuario aleatorio
        username=nombre[0:3]+apellido[0:3]
        usuario.username=username
        #Envio del correo al usuario
        correoAdmin=settings.EMAIL_HOST_USER
        subject="Datos de ingreso"
        message='Datos de ingreso al sistema. \nNombre del usuario: {} \nCorreo del usuario: {} \nContraseña: {}'.format(nombre,correo,password1)
        send_mail(subject,message,correoAdmin,[correo])
        usuario.set_password(password1)
        if commit:
            usuario.save()
        return usuario

class FormAbogado(forms.ModelForm):
    class Meta:
        model= Abogado
        fields=('nombre', 'apellido', 'dui', 'direccion', 'estado_civil', 'correo', 'telefono', 'fecha_nacimiento', 'Tipo_de_abogado')
        widgets={
                 'nombre': forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese nombre',
                         'id':'nombre',
                     }
                 ),
                 'apellido':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese apellido',
                         'id':'descripcion',
                     }
                 ),
                 'correo':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese correo',
                         'id':'descripcion',
                     }
                 ),
                 'direccion':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese direccion',
                         'id':'descripcion',
                     }
                 ),
                 'telefono':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese telefono',
                         'id':'descripcion',
                     }
                 ),
                 'dui': forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese numero de dui',
                         'id':'dui',
                     }
                ),
                 'estado_civil':forms.Select(
                      attrs={
                         'id':'estado_civil',
                          'class':'form-control form-control-sm col-sm-2'
                    }
                ),
                 'fecha_nacimiento':forms.SelectDateWidget(
                     years=range(1900, 2020),
                     attrs={
                         'class':'form-control form-control-sm col-sm-2',
                         'type': 'date',
                         'id':'fecha_nacimiento'
                         }
                ),
                'Tipo_de_abogado':forms.Select(
                      attrs={
                        'id':'Tipo_de_abogado',
                        'class':'form-control form-control-sm col-sm-2'
                      }
                 )
             }
        
    def save(self,commit=True):
        #crea una contraseña aleatoria
        password1=BaseUserManager().make_random_password(15)
        #Captura datos
        nombre=self.cleaned_data.get("nombre")
        apellido=self.cleaned_data.get("apellido")
        correo=self.cleaned_data.get("correo")
        usuario=super().save(commit=False)

        #se agrega el rol de una vez
        usuario.rol=Rol.objects.get(id=2)
        
        #Se crea un usuario aleatorio y se asigna
        username=nombre[0:3]+apellido[0:3]
        usuario.username=username
        
        #Envio del correo al usuario
        correoAdmin=settings.EMAIL_HOST_USER
        subject="Datos de ingreso"
        message='Datos de ingreso al sistema. \nNombre del usuario: {} \nCorreo del usuario: {} \nContraseña: {}'.format(nombre,correo,password1)
        send_mail(subject,message,correoAdmin,[correo])
        
        usuario.set_password(password1)
        if commit:
            usuario.save()
        return usuario

class InstitucionForm(forms.ModelForm):
    class Meta:
        model=Institucion
        fields='__all__'
        labels={
            'nombre': 'Nombre de la institucion',
            'direccion': 'Direccion de la institucion',
            'descripcion':'Descripcion',
            'correo':'correo',
            'telefono':'Telefono',
            'tipo':'Tipo de institucion',
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre de la institucion',
                    'id':'nombre',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese la direccion de la institucion',
                    'id':'direccion',
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese descripcion de la institucion',
                    'rows': '3',
                    'id':'descripcion',
                }
            ),
            
            'correo': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el correo de la institucion',
                    'id':'correo',
                }
            ),

            'telefono': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el telefono de la institucion',
                    'id':'telefono',
                }
            ),
            'tipo': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el tipo de institucion',
                    'id':'tipo',
                }
            ),
        }

