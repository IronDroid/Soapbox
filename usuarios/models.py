from django.db import models
from django.contrib.auth.models import User

class Administrador(models.Model):
    cargo = models.CharField(max_length=20, blank=True)
    nivel = models.IntegerField(blank=True, null=True)
    user = models.OneToOneField(User, blank=True, null=True)

    class Meta:
        db_table = 'administrador'

    def __unicode__(self):
        return self.user.username

class Usuario(models.Model):
    institucion = models.CharField(max_length=25, blank=True)
    tipo = models.CharField(max_length=25, blank=True)
    user = models.OneToOneField(User, blank=True, null=True)
    urlqr = models.URLField(blank=True)

    class Meta:
        db_table = 'usuario'

    def __unicode__(self):
        return self.user.username
