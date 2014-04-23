from django.db import models

class Persona(models.Model):
    ci = models.IntegerField(primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        db_table = 'persona'

    def __unicode__(self):
        return self.persona.nombre_completo

class Administrador(models.Model):
    cargo = models.CharField(max_length=20, blank=True)
    nivel = models.IntegerField(blank=True, null=True)
    persona = models.OneToOneField(Persona, blank=True, null=True)

    class Meta:
        db_table = 'administrador'

    def __unicode__(self):
        return self.persona.nombre_completo

class Usuario(models.Model):
    institucion = models.CharField(max_length=25, blank=True)
    tipo = models.CharField(max_length=25, blank=True)
    persona = models.OneToOneField(Persona, blank=True, null=True)
    urlqr = models.URLField(blank=True)

    class Meta:
        db_table = 'usuario'

    def __unicode__(self):
        return self.persona.nombre_completo
