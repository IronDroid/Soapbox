from django.db import models
from usuarios.models import Usuario

class Tipo(models.Model):
    nombre = models.CharField(max_length=25, blank=True)
    descripcion = models.CharField(max_length=25, blank=True)

    class Meta:
        db_table = 'tipo'

class Producto(models.Model):
    puntuacion = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=40, blank=True)
    costo = models.FloatField(blank=True, null=True)
    tipo_producto = models.ForeignKey(Tipo)

    class Meta:
        db_table = 'producto'

    def __unicode__(self):
        return self.nombre

class Compra(models.Model):
    idusuario = models.ForeignKey(Usuario, blank=True, null=True)
    idproducto = models.ForeignKey(Producto, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'compra'

class Reserva(models.Model):
    fecha_reserva = models.DateField(blank=True, null=True)
    idproducto = models.ForeignKey(Producto, blank=True, null=True)
    idusuario = models.ForeignKey(Usuario, blank=True, null=True)

    class Meta:
        db_table = 'reserva'