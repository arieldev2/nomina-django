from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Nomina(models.Model):
	empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE)
	salario_base = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	dias_laborados = models.IntegerField(default=0)
	salario_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	fecha = models.DateTimeField(default=timezone.now)

	def calcular_salario(self):
		salario_total = self.salario_base * self.dias_laborados
		return salario_total

	def save(self, *args, **kwargs):
		self.salario_total = self.calcular_salario()
		super().save(*args, **kwargs)



	def get_absolute_url(self):
		return reverse('nomina-detalles', kwargs={'pk': self.pk})

	@property
	def Nombre_completo(self):
		return '{} {} {}'.format(self.empleado.nombre, self.empleado.primer_apellido, self.empleado.segundo_apellido)

	@property
	def clave_emp(self):
		return self.empleado.clave_empleado



class Empleado(models.Model):

	areas = (
		('Administracion', 'Administracion'),
		('Aduanas', 'Aduanas'),
		('Negocios', 'Negocios'),
		('Mercadotecnia', 'Mercadotecnia'),
		('Relaciones Publicas', 'Relaciones Publicas'),
		('Mantenimiento', 'Mantenimiento'),
		('Ingenieria', 'Ingenieria'),
		('Diseño', 'Diseño'),
		)

	puestos = (
		('Documentador','Documentador'),
		('Import-Export','Import-Export'),
		('Vendedor','Vendedor'),
		('Social Manager','Social Manager'),
		('RP','RP'),
		('Control de Higiene','Control de Higiene'),
		('Produccion','Produccion'),
		('Imagen Corporativa', 'Imagen Corporativa'),
		)

	clave_empleado = models.CharField(max_length=50)
	nombre = models.CharField(max_length=200)
	primer_apellido = models.CharField(max_length=200)
	segundo_apellido = models.CharField(max_length=200)
	edad = models.IntegerField()
	area = models.CharField(max_length=100, choices=areas, default='Administracion')
	puesto = models.CharField(max_length=100, choices=puestos, default='Documentador')
	fecha_registro = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.nombre

	@property
	def Nombre_completo(self):
		return '{} {} {}'.format(self.nombre, self.primer_apellido, self.segundo_apellido)

	def get_absolute_url(self):
		return reverse('empleado-detalles', kwargs={'pk': self.pk})


