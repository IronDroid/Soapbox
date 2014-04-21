from django.contrib import admin
from .models import Compra, Reserva, Producto, Tipo

admin.site.register(Compra)
admin.site.register(Producto)
admin.site.register(Reserva)
admin.site.register(Tipo)
