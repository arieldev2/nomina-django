from django.contrib import admin
from .models import Nomina, Empleado


class NominaNewView(admin.ModelAdmin):
	list_display = ('clave_emp', 'Nombre_completo', 'salario_base', 'dias_laborados', 'salario_total', 'fecha')
	search_fields = ('empleado',)

admin.site.register(Nomina, NominaNewView)



class EmpleadoNewView(admin.ModelAdmin):
	list_display = ('clave_empleado', 'nombre', 'primer_apellido', 'segundo_apellido', 'area', 'puesto', 'fecha_registro')
	search_fields = ('clave_empleado', 'nombre', 'primer_apellido', 'segundo_apellido',)

admin.site.register(Empleado, EmpleadoNewView)

