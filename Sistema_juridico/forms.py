from django import forms
from .models import TipoDeAbogado, Caso, TipoDeProceso
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User #Usuario

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
                    'id':'descripcion',
                }
            ),
        }
    
    
class FormLogin(AuthenticationForm):
    class Meta:
        db_table = User
        fields=['username','password']
        labels={
            'username': 'Nombre del tipo',
            'password':'Contraseña'
        }
    
        widgets={
            'username': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del tipo ',
                    'id':'username'
                }
            ),
            'descripcion':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese contraseña',
                    'id':'password',
                }
            ),
        }
    def __init__(self, *args, **kwargs):
        super(FormLogin, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
    


class CasoForm(forms.ModelForm):
        
    class Meta:
        model=Caso
        fields='__all__'
        labels={
            'codigo': 'Codigo',
            'descripcion':'Descripcion'
        }
        widgets={
            'codigo': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el codigo del caso',
                    'id':'codigo',
                    
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese descripcion del tipo de abogado',
                    'id':'descripcion',
                }
            ),
            'estado':forms.Select(
                attrs={
                    'id':'estado',
                    'class':'form-control form-control-sm col-sm-2'
                }
            ),
            'tipo_de_proceso':forms.Select(
                attrs={
                    'id':'tipo_de_proceso',
                    'class':'form-control form-control-sm col-sm-2'
                }
            ),
            
            
        }
        
class TipoDeProcesoForm(forms.ModelForm):
    class Meta:
        model=TipoDeProceso
        fields='__all__'
        