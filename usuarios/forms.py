#encoding:utf-8

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from usuarios.models import Usuario, Administrador

class UsuarioForm(ModelForm):
	class Meta:
		model = Usuario

class AdministradorForm(ModelForm):
	class Meta:
		model = Administrador
