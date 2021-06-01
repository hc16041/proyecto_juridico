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


class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,
                    'class':'form-control',
                    'placeholder':'Ingrese el correo ',
                    'id':'correo'
                }))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese la contraseña ',
                    'id':'contraseña'
                }),
    )

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

        # Set the max length and label for the "username" field.
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        self.fields['username'].max_length = self.username_field.max_length or 254
        if self.fields['username'].label is None:
            self.fields['username'].label = capfirst(self.username_field.verbose_name)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``forms.ValidationError``.

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self):
        return forms.ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            params={'username': self.username_field.verbose_name},
        )

class PasswordResetForm(forms.Form):
    correo = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True,
                    'class':'form-control',
                    'placeholder':'Ingrese el correo ',
                    'id':'correo'
                }),label=("Correo"), max_length=254)


    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        """
        Send a django.core.mail.EmailMultiAlternatives to `to_email`.
        """
        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)

        email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
        if html_email_template_name is not None:
            html_email = loader.render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, 'text/html')

        email_message.send()

    def get_users(self, correo):
        """Given an email, return matching user(s) who should receive a reset.

        This allows subclasses to more easily customize the default policies
        that prevent inactive users and users with unusable passwords from
        resetting their password.
        """
        active_users = UserModel._default_manager.filter(**{
            '%s__iexact' % UserModel.get_correo_field_name(): correo,
            'is_active': True,
        })
        return (u for u in active_users if u.has_usable_password())

    def save(self, domain_override=None,
             subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/password_reset_email.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None, html_email_template_name=None,
             extra_email_context=None):
        """
        Generate a one-use only link for resetting password and send it to the
        user.
        """
        correo = self.cleaned_data["correo"]
        for user in self.get_users(correo):
            if not domain_override:
                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override
            context = {
                'correo': correo,
                'domain': domain,
                'site_name': site_name,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'user': user,
                'token': token_generator.make_token(user),
                'protocol': 'https' if use_https else 'http',
                **(extra_email_context or {}),
            }
            self.send_mail(
                subject_template_name, email_template_name, context, from_email,
                correo, html_email_template_name=html_email_template_name,
            )

