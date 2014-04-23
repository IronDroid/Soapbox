from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from .views import UsuarioCreateView

urlpatterns = patterns('',
	# url(r'^$', UsuarioCreateView.as_view(), name='home'),
	url(r'^webflow/$', 'usuarios.views.webflow', name='webflow'),
)
