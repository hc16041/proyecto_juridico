from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import Permission, User #Usuario
from django.contrib.auth.hashers import make_password 

#Para registrar superusuarios
class FormRegistro(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'password',
        }
        ),max_length = 150)
    password1 = forms.CharField(label='Confirm password',widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'confirm password',
        }
        ),max_length = 150)

    class Meta:
        model=Usuario
        fields=('correo','nombre')
    
    
    def clean_email(self):
        correo=self.cleaned_data.get('correo')
        qs=Usuario.objects.filter(correo=correo)
        if qs.exists():
            raise forms.ValidationError("Correo ya registrado")
        return correo
    
    def clean_password2(self):
        password1=self.clean_data.get("password1")
        password2=self.clean_data.get("password2")
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("Contraseñas no coinciden")
        return password2
    
#Para actualizar usuario
class FormActualizarUsuario(forms.ModelForm):
    password=ReadOnlyPasswordHashField()
    class Meta:
        model = Usuario
        fields = ('correo','password','nombre','apellido')
    
    def clean_password(self):
        return self.initial['password']

#Login
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
    # def __init__(self, *args, **kwargs):
    #     super(FormLogin, self).__init__(*args,**kwargs)
    #     self.fields['username'].widget.attrs['class'] = 'form-control'
    #     self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
    #     self.fields['password'].widget.attrs['class'] = 'form-control'
    #     self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

#Form para contacto Email
class contactoForm(forms.Form):
    origen=forms.CharField()
    asunto=forms.CharField(required=True)
    destino=forms.EmailField()
    contenido=forms.CharField(max_length=999, widget=forms.Textarea)

#Form Usuario 
class FormUsuario(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Contraseña',
            'id':'password1',
            'required':'required'
        }
        ))
    password2 = forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Confirmar Contraseña',
            'id':'password2',
            'required':'required'
        }
        ))
    class Meta:
        model=Usuario
        fields=('correo','nombre','apellido',)
        widgets={
                 'nombre': forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese el nombre',
                         'id':'nombre',
                       
                     }
                 ),
                 'correo':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese correo',
                         'id':'descripcion',
                     }
                 ),
                 'apellido':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese apellido',
                         'id':'descripcion',
                     }
                 ),
                 'direccion':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese la direccion',
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
             }
       
    def clean_password2(self):
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")
        if password1!=password2:
            raise forms.ValidationError("Contraseñas no coinciden")
        return password2
    
    def save(self,commit=True):
         #guarda contraseña en formato Hash
        usuario=super().save(commit=False)
        usuario.set_password(self.cleaned_data["password1"])
        if commit:
            usuario.save()
        return usuario

#Forms mostrados directamente en el sistema
class CasoForm(forms.ModelForm):
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
                    #'disabled': 'true',
                }
            ),
            'rol_cliente': forms.Select(
                attrs={
                    'id':'rol_cliente',
                    'class':'form-control form-control-sm col-sm-6',
                }
            ),
            'id_abogado': forms.Select(
                attrs={
                    'id':'id_abogado',
                    'class':'form-control form-control-sm col-sm-6',
                }
            ),
            'codigo_caso': forms.NumberInput(
                attrs={
                    'class':'form-control form-control-sm col-sm-6',
                    'placeholder':'Ingrese el codigo del caso',
                    'id':'codigo_caso',
                    'min':'1'
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm col-sm-6',
                    'placeholder':'Ingrese descripcion detallada sobre el caso',
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
            'pago_caso':forms.TextInput(
                attrs={
                    'id':'pago_caso',
                    'class':'form-control form-control-sm col-sm-6'
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
                     }
            ),
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
    def clean_password2(self):
        password1=make_password('')
        # password2=self.cleaned_data.get("password2")
        # if password1!=password2:
        #     raise forms.ValidationError("Contraseñas no coinciden")
        # return password2
    
    
    def save(self,commit=True):
         #guarda contraseña en formato Hash
         #crea una contraseña aleatoria
        password1=BaseUserManager().make_random_password(15)
        print(password1)
        nombre=self.cleaned_data.get("nombre")
        apellido=self.cleaned_data.get("apellido")
        correo=self.cleaned_data.get("correo")
        usuario=super().save(commit=False)
        #se agrega el rol de una vez
        usuario.rol=Rol.objects.get(id=1)
        #Se crea un usuario aleatorio
        username=nombre[0:3]+apellido[0:3]
        usuario.username=username
        
        usuario.set_password(password1)
        if commit:
            usuario.save()
        return usuario

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
       
    def clean_password2(self):
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")
        if password1!=password2:
            raise forms.ValidationError("Contraseñas no coinciden")
        return password2
    
    def save(self,commit=True):
         #guarda contraseña en formato Hash
         #crea una contraseña aleatoria
        password1=BaseUserManager().make_random_password(15)
        print(password1)
        nombre=self.cleaned_data.get("nombre")
        apellido=self.cleaned_data.get("apellido")
        correo=self.cleaned_data.get("correo")
        usuario=super().save(commit=False)
        #se agrega el rol de una vez
        usuario.rol=Rol.objects.get(id=2)
        #Se crea un usuario aleatorio
        username=nombre[0:3]+apellido[0:3]
        usuario.username=username
        
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
            'correo':'Correo',
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
                    'placeholder':'Ingrese el email de la institucion',
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


