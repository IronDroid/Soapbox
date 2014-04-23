from django.shortcuts import render
from django.views.generic import CreateView

from .models import Usuario
from .forms import UsuarioForm

def webflow(request):
	return render(request, 'Webflow.html')

class UsuarioCreateView(CreateView):
	template_name = 'Webflow.html'
	# model = Usuario
	# form_class = UsuarioForm