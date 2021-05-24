from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.datetime_safe import datetime
from django.contrib.admin import widgets
# Create your models here.



class TipoDeAbogado(models.Model):
    nombre = models.CharField(max_length = 100, blank=False, null=False)
    descripcion = models.TextField(max_length = 220, blank=False, null=False)
    fecha_creacion = models.DateField('Fecha de creacion',auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name = 'Tipo de abogado'
        verbose_name_plural = 'Tipos de abogados'
        ordering=['nombre']
        
    def __str__(self):
        return self.nombre
    
class TipoDeProceso(models.Model):
    nombre = models.CharField(max_length = 100, blank=False, null=False)
    descripcion = models.TextField(max_length = 220, blank=False, null=False)
    fecha_creacion = models.DateField('Fecha de creacion',auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name = 'Tipo de proceso'
        verbose_name_plural = 'Tipos de procesos'
        ordering=['nombre']
        
    def __str__(self):
        return self.nombre
    
class Institucion(models.Model):
    nombre = models.CharField(max_length = 150,blank=False, null=False)
    direccion = models.CharField(max_length = 150,blank=False, null=False)
    descripcion = models.TextField(max_length = 220, blank=False, null=False)
    correo = models.EmailField(max_length=150,blank=False, null=False)
    telefono = models.IntegerField()
    tipo = models.CharField(max_length = 150,blank=False, null=False)
    fecha_creacion = models.DateField('Fecha de creacion',auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name = 'Institucion'
        verbose_name_plural = 'Instituciones'

    def __str__(self):
        return self.nombre

class Audiencia(models.Model):
    detalle = models.CharField(max_length = 150,blank=False,null=False)
    fecha = models.DateField()
    hora = models.DateTimeField()
    descripcion = models.TextField(max_length = 220, blank=False, null=False)
    fecha_creacion = models.DateField('Fecha de creacion',auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name = 'Audiencia'
        verbose_name_plural = 'Audiencias'

    def __str__(self):
        return self.detalle

class FormaDePago(models.Model):
    tipo = models.CharField(max_length = 150,blank=False, null=False)
    plazo = models.IntegerField()
    cuota = models.IntegerField()
    monto=models.DecimalField( max_digits=5, decimal_places=2)
    fecha_creacion = models.DateField('Fecha de creacion',auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name = 'Forma De Pago'
        verbose_name_plural = 'Forma De Pagos'

    def __str__(self):
        return self.tipo

class Pago(models.Model):
    fecha = models.DateField()
    descripcion = models.TextField(max_length = 220, blank=False, null=False)
    cargo = models.DecimalField(max_digits=5, decimal_places=2)
    monto = models.DecimalField(max_digits=6, decimal_places=2)
    saldo_total = models.DecimalField(max_digits=6, decimal_places=2)
    tipo_de_pago=models.ForeignKey(FormaDePago, blank=False, null=False,on_delete=models.CASCADE)
    fecha_creacion = models.DateField('Fecha de creacion',auto_now=True, auto_now_add=False)
    
    class Meta:
        """Meta definition for Pago."""

        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'

    def __str__(self):
        """Unicode representation of Pago."""
        return self.descripcion


class ManejadorUsuario(BaseUserManager):
      def create_user(self,correo,nombre,apellido,password=None):
          if not correo:
              raise ValueError('Usuarios deben tener un correo electronico valido')
          usuario=self.model(
              correo=self.normalize_email(correo),
              nombre=nombre,
              apellido=apellido
              )
          
          usuario.set_password(password)
          usuario.save(using=self._db)
          return usuario
      
    #   def create_staffuser(self,correo,apellido, nombre, password):
    #       usuario=self.create_user(
    #           correo,
    #           nombre=nombre,
    #           apellido=apellido,
    #           password=password,
    #       )
    #       usuario.staff=True
    #       usuario.save(using=self._db)
    #       return usuario
      
      def create_superuser(self,correo,nombre, apellido,password):
          usuario=self.create_user(
              correo,
              nombre=nombre,
              apellido=apellido,
              password=password
          )
          usuario.usuario_administrador=True
          usuario.save(using=self._db)
          return usuario

Estado_Civil= (
    (0, "Soltero"),
    (1, "Casado"),
    (2,"Divorciado")
)
class Usuario(AbstractBaseUser,PermissionsMixin):
    correo = models.EmailField(verbose_name='correo electronico',max_length=100,unique=True)
    nombre = models.CharField(max_length = 150)
    apellido = models.CharField(max_length = 150)
    direccion = models.CharField(max_length = 150)
    dui = models.CharField(max_length = 10, unique=True)
    telefono=models.CharField(max_length = 8)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)
    fecha_nacimiento = models.DateField(null=True)
    estado_civil = models.IntegerField(choices=Estado_Civil, default=0)
    username=models.CharField( max_length=50)
    usuario_activo=models.BooleanField(default=True)
    usuario_administrador=models.BooleanField(default=False)
    
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
    
    def has_perm(self,perm,obj=None):
        "El usuario cuenta con permiso en especifico?"
        return True
    
    def has_module_perms(self,app_label):
        "El usuario cuenta con los permisos para ver una app en especifico"
        return True
    
    @property
    def is_staff(self):
        "El usuario es staff(no super usuario)?"
        return self.usuario_administrador
    
    # @property
    # def is_admin(self):
    #     "El usuario es admin(super usuario)?"
    #     return self.admin
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido + ' ' + self.correo

Rol_Cliente= (
    (0, "Demandante"),
    (1,"Demandado")
)
class Cliente(Usuario):
    rol_cliente = models.IntegerField(choices=Rol_Cliente, default=0)
    #es_cliente=models.BooleanField(default=False)

class Abogado(Usuario):

   Tipo_de_abogado=models.OneToOneField(TipoDeAbogado, verbose_name=("Tipo De Abogado"), on_delete=models.CASCADE)
    #es_abogado=models.BooleanField(default=False)
    
    

Estados = (
    ('P', 'En Proceso'),
    ('F', 'Finalizado')
)
class Caso(models.Model):
    id_cliente=models.ForeignKey(Cliente, verbose_name=("Id Cliente"), on_delete=models.CASCADE)
    id_abogado=models.ForeignKey(Abogado, verbose_name=("Id Abogado"), on_delete=models.CASCADE)
    codigo = models.IntegerField(primary_key=True,blank=False, null=False)
    descripcion = models.TextField(max_length = 220, blank=False, null=False)
    estado = models.CharField(choices=Estados, default=0, max_length=2)
    tipo_de_proceso = models.ForeignKey(TipoDeProceso,on_delete=models.CASCADE)
    pago=models.ForeignKey(Pago,on_delete=models.CASCADE)
    audiencia=models.ForeignKey(Audiencia,on_delete=models.CASCADE)
    fecha_creacion = models.DateField('Fecha de creacion',auto_now=True, auto_now_add=False)
    
    
    class Meta:
        verbose_name = 'Caso'
        verbose_name_plural = 'Casos'

    def __str__(self):
        """Unicode representation of Caso."""
        return self.codigo
    
class Reporte(models.Model):
    codigo_caso=models.ForeignKey(Caso,verbose_name="codigo caso"),on_delete=models.CASCADE
    dui_cliente=models.ForeignKey(Cliente, verbose_name=("Id Cliente"), on_delete=models.CASCADE)
    nombre_abogado=models.ForeignKey(Abogado, verbose_name=("Id Abogado"), on_delete=models.CASCADE)
    codigo = models.IntegerField(primary_key=True,blank=False, null=False)
    estado_cliente = models.IntegerField(choices=Estados, default=0)
    tipo_de_proceso = models.ForeignKey(TipoDeProceso,on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reporte'

    def __str__(self):
        """Unicode representation of Caso."""
        return self.codigo
    