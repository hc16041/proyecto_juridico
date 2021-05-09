from django.db import models

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
        return self.cargo

Estados = (
    (0, "En Proceso"),
    (1, "Finalizado")
)
class Caso(models.Model):
    codigo = models.IntegerField(primary_key=True,blank=False, null=False)
    descripcion = models.TextField(max_length = 220, blank=False, null=False)
    estado = models.IntegerField(choices=Estados, default=0)
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
    