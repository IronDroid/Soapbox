from django.db import models
from usuarios.models import Usuario

class Seminario(models.Model):
    fecha_realizacion = models.DateTimeField(blank=True, null=True)
    tema = models.CharField(max_length=100, blank=True)
    poniente = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'seminario'


class Asiste(models.Model):
    idseminario = models.ForeignKey(Seminario, blank=True, null=True)
    idusuario = models.ForeignKey(Usuario, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)

    class Meta:
        db_table = 'asiste'
