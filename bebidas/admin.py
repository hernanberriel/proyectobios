from django.contrib import admin
from bebidas.models import *


# Register your models here.
class DistribuidorAdmin(admin.ModelAdmin):
	list_display=('nombre', 'rut', 'telefono')
	search_fields= ('nombre', 'rut', 'telefono')
	ordering=('nombre',)

class BebidaAdmin(admin.ModelAdmin):
	search_fields=('marca', 'categoria')
	list_display=('marca', 'categoria', 'contenido_neto', 'stock')

admin.site.register(Distribuidor, DistribuidorAdmin)
admin.site.register(Bebida, BebidaAdmin)