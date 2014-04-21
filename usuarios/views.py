from django.shortcuts import render
from django.views.generic import CreateView

from .models import Usuario
from .forms import UsuarioForm

class UsuarioCreateView(CreateView):
	template_name = 'usuario_form.html'
	model = Usuario
	form_class = UsuarioForm