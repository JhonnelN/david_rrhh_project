from django.contrib import admin
from.models import Departamento, Empleado, Solicitud

# Cambia el nombre de la administración
admin.site.site_title = "Panel de Administración SRH"
admin.site.site_header = "Panel de Administración SRH"
admin.site.index_title = "Bienvenido a Panel de Administración SRH"

# Register your models here.
admin.site.register(Departamento)
admin.site.register(Empleado)
admin.site.register(Solicitud)


