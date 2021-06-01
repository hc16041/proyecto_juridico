from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)
from django.contrib.auth.models import Group, Permission, PermissionsMixin
from django.utils import timezone
from django.utils.datetime_safe import datetime
from django.contrib.admin import widgets
from django.contrib.contenttypes.models import ContentType
from django.core.validators import RegexValidator
from django.core.mail import send_mail
# Create your models here.



class TipoDeAbogado(models.Model):
    nombre = models.CharField(max_length = 100, blank=False, null=False,validators=[RegexValidator("[a-zA-Z]+[ a-zA-Z-_]*$",message="Introduzca letras del alfabeto")])
    descripcion = models.TextField(max_length = 220, blank=False, null=False)
    fecha_creacion = models.DateField('Fecha de creacion',auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name = 'Tipo de abogado'
        verbose_name_plural = 'Tipos de abogados'
        ordering=['nombre']
        
    def __str__(self):
        return self.nombre
    
class TipoDeProceso(models.Model):
    nombre = models.CharField(max_length = 100, blank=False, null=False,validators=[RegexValidator("[a-zA-Z]+[ a-zA-Z-_]*$",message="Introduzca letras del alfabeto")])
    descripcion = models.TextField(max_length = 220, blank=False, null=False)
    fecha_creacion = models.DateField('Fecha de creacion',auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name = 'Tipo de proceso'
        verbose_name_plural = 'Tipos de procesos'
        ordering=['nombre']
        permissions = (("can_view_tipodeproceso", "Ver tipos de proceso"),) 
        
    def __str__(self):
        return self.nombre
    
class Institucion(models.Model):
    nombre = models.CharField(max_length = 150,blank=False, null=False,validators=[RegexValidator("[a-zA-Z]+[ a-zA-Z-_]*$",message="Introduzca letras del alfabeto")])
    direccion = models.CharField(max_length = 150,blank=False, null=False)
    descripcion = models.TextField(max_length = 220, blank=False, null=False)
    correo = models.EmailField(max_length=150,blank=False, null=False)
    telefono = models.CharField(max_length = 9,validators=[RegexValidator("^\d{4}-\d{4}$",message="Telefono invalido")])
    tipo = models.CharField(max_length = 150,blank=False, null=False)
    fecha_creacion = models.DateField('Fecha de creacion',auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name = 'Institucion'
        verbose_name_plural = 'Instituciones'

    def __str__(self):
        return self.nombre

class Rol(models.Model):
    """Model definition for Rol."""

    # TODO: Define fields here
    id = models.AutoField(primary_key = True)
    rol = models.CharField('Rol', max_length=50,unique = True)

    class Meta:
        """Meta definition for Rol."""

        verbose_name = 'Rol'
        verbose_name_plural = 'Rols'

    def __str__(self):
        """Unicode representation of Rol."""
        return self.rol
    
    def save(self,*args,**kwargs):
        permisos_defecto = ['add','change','delete','view']
        if not self.id:
            nuevo_grupo,creado = Group.objects.get_or_create(name = f'{self.rol}')
            for permiso_temp in permisos_defecto:
                permiso,created = Permission.objects.update_or_create(
                    name = f'Can {permiso_temp} {self.rol}',
                    content_type = ContentType.objects.get_for_model(Rol),
                    codename = f'{permiso_temp}_{self.rol}'
                )
                if creado:
                    nuevo_grupo.permissions.add(permiso.id)
            super().save(*args,**kwargs)
        else:
            rol_antiguo = Rol.objects.filter(id = self.id).values('rol').first()
            if rol_antiguo['rol'] == self.rol:
                super().save(*args,**kwargs)
            else:
                Group.objects.filter(name = rol_antiguo['rol']).update(name = f'{self.rol}')
                for permiso_temp in permisos_defecto:
                    Permission.objects.filter(codename = f"{permiso_temp}_{rol_antiguo['rol']}").update(
                        codename = f'{permiso_temp}_{self.rol}',
                        name = f'Can {permiso_temp} {self.rol}'
                    )
                super().save(*args,**kwargs)
                 
class ManejadorUsuario(BaseUserManager):
    def _create_user(self,nombre, apellido,correo, password, **extra_fields):
        """
        Create and save a user with the given username, correo, and password.
        """
        if not correo:
            raise ValueError('The given correo must be set')
        correo = self.normalize_email(correo)
        user = self.model(nombre=nombre,apellido=apellido, correo=correo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,nombre, apellido,correo=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(nombre, apellido,correo, password, **extra_fields)

    def create_superuser(self, nombre, apellido,correo, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(nombre, apellido,correo, password, **extra_fields)

Estado_Civil= (
    ("Soltero", "Soltero"),
    ("Casado", "Casado"),
    ("Divorciado","Divorciado"),
    ("Viudo", "Viudo"),
    ("Separado", "Separado")
)
class Usuario(AbstractBaseUser, PermissionsMixin):
    correo = models.EmailField(verbose_name='correo electronico',max_length=100,unique=True)
    nombre= models.CharField(max_length = 150,validators=[RegexValidator("[a-zA-Z]+[ a-zA-Z-_]*$",message="Introduzca letras del alfabeto")])
    apellido = models.CharField(max_length = 150,validators=[RegexValidator("[a-zA-Z]+[ a-zA-Z-_]*$",message="Introduzca letras del alfabeto")])
    direccion = models.CharField(max_length = 150)
    dui = models.CharField(max_length = 10, validators=[RegexValidator("^\d{8}-\d{1}$",message="Dui invalido")])
    telefono=models.CharField(max_length = 9,validators=[RegexValidator("^\d{4}-\d{4}$",message="Telefono invalido")])
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)
    fecha_nacimiento = models.DateField(null=True)
    estado_civil = models.CharField(choices=Estado_Civil, max_length=220)
    username=models.CharField( max_length=50)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE,blank = True,null = True)
    is_active = models.BooleanField(
        ('active'),
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_superuser=models.BooleanField(default=False)
    is_staff = models.BooleanField(
        ('staff status'),
        default=False,
        help_text=('Designates whether the user can log into this admin site.'),
    )
    
    
    objects=ManejadorUsuario()
    
    USERNAME_FIELD='correo'
    REQUIRED_FIELDS=['nombre','apellido']
    
    class meta:
        verbose_name='usuario'
        verbose_name_plural='usuarios'
        
    def get_full_name(self):
        full_name = '%s %s' % (self.nombre, self.apellido)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.nombre
    
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido + ' ' + self.correo
    
    def save(self,*args,**kwargs):
        if not self.id:
            super().save(*args,**kwargs)
            if self.rol is not None:
                grupo = Group.objects.filter(name = self.rol.rol).first()
                print(grupo)
                if grupo:
                    self.groups.add(grupo)
                super().save(*args,**kwargs)
        else:
            if self.rol is not None:
                grupo_antiguo = Usuario.objects.filter(id = self.id).values('rol__rol').first()
                print(grupo_antiguo['rol__rol'])
                print(self.rol.rol)
                if grupo_antiguo['rol__rol'] == self.rol.rol:
                    print("Entro en igualdad de roles")
                    super().save(*args,**kwargs)
                else:
                    grupo_anterior = Group.objects.filter(name = grupo_antiguo['rol__rol']).first()
                    if grupo_anterior:
                        print(grupo_anterior)
                        self.groups.remove(grupo_anterior)
                    nuevo_grupo = Group.objects.filter(name = self.rol.rol).first()
                    if nuevo_grupo:
                        self.groups.add(nuevo_grupo)
                    super().save(*args,**kwargs)
    

class Cliente(Usuario):
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
class Abogado(Usuario):
    Tipo_de_abogado=models.ForeignKey(TipoDeAbogado, verbose_name=("Tipo De Abogado"), on_delete=models.CASCADE)
    


Estados = (
    ("En Proceso", "En Proceso"),
    ("Finalizado", "Finalizado")
)

Rol_Cliente= (
    ("Demandante", "Demandante"),
    ("Demandado", "Demandado")
)

Tipo_Pago =(
    ("Contado", "Contado"),
    ("Credito", "Credito")
)
class Caso(models.Model):
    id_cliente=models.ForeignKey(Cliente, verbose_name=("Id Cliente:"), on_delete=models.CASCADE)
    id_abogado=models.ForeignKey(Abogado, verbose_name=("Id Abogado"), on_delete=models.CASCADE)
    codigo_caso= models.CharField(primary_key=True, max_length=10)
    rol_cliente = models.CharField(choices=Rol_Cliente, max_length=220)
    descripcion = models.TextField(max_length = 220, blank=False, null=False)
    estado = models.CharField(choices=Estados, max_length=220)
    tipo_de_proceso = models.ForeignKey(TipoDeProceso,on_delete=models.CASCADE)
    pago_caso = models.FloatField( max_length=220)
    fecha_creacion = models.DateField('Fecha de creacion',auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name = 'Caso'
        verbose_name_plural = 'Casos'

    
    def __str__(self):
        return self.codigo_caso

Detalle =(
    ("Nuevo", "Nuevo"),
    ("Reprogramado", "Reprogramado")
)

class Audiencia(models.Model):
    id = models.AutoField(primary_key = True)
    codigo_caso= models.ForeignKey(Caso, on_delete=models.CASCADE)
    id_cliente=models.ForeignKey(Cliente, on_delete= models.CASCADE)
    detalle = models.CharField(choices=Detalle, max_length=220)
    fecha = models.DateField()
    hora = models.TimeField()
    juzgado= models.ForeignKey(Institucion, on_delete=models.CASCADE,blank = True,null = True)
    descripcion = models.TextField(max_length = 220, blank=False, null=False)
    fecha_creacion = models.DateField('Fecha de creacion',auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name = 'Audiencia'
        verbose_name_plural = 'Audiencias'

    def __str__(self):
        return self.detalle

class Pago(models.Model):
    fecha = models.DateField()
    codigo_caso = models.ForeignKey(Caso, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length = 220, blank=False, null=False)
    monto = models.DecimalField(max_digits=6, decimal_places=2)
    fecha_creacion = models.DateField('Fecha de creacion',auto_now=True, auto_now_add=False)
    
    class Meta:
        """Meta definition for Pago."""

        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'

    def __str__(self):
        """Unicode representation of Pago."""
        return self.descripcion