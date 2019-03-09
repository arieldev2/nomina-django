from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Nomina, Empleado
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def Home(request):
	return render(request, 'empleados/home.html')


class NominaListView(LoginRequiredMixin, ListView):
	model = Nomina
	template_name = 'empleados/index.html'
	context_object_name = 'items'
	ordering = ['-fecha']
	paginate_by = 2

class NominaDetailView(LoginRequiredMixin, DetailView):
	model = Nomina

class NominaCreateView(LoginRequiredMixin, CreateView):
	model = Nomina
	fields = ['empleado', 'salario_base', 'dias_laborados']



class NominaUpdateView(LoginRequiredMixin, UpdateView):
	model = Nomina
	fields = ['empleado', 'salario_base', 'dias_laborados']

class NominaDeleteView(LoginRequiredMixin, DeleteView):
	model = Nomina
	success_url = '/nomina'

class NominaSearchView(LoginRequiredMixin, ListView):
	model = Nomina
	template_name = 'empleados/nomina_empleado.html'
	context_object_name = 'items'


	def get_queryset(self):
		empleado = get_object_or_404(Empleado, clave_empleado=self.kwargs.get('clave_empleado'))
		return Nomina.objects.filter(empleado=empleado).order_by('-fecha')




class EmpleadoListView(LoginRequiredMixin, ListView):
	model = Empleado
	template_name = 'empleados/index_empleado.html'
	context_object_name = 'items'
	ordering = ['-fecha_registro']
	paginate_by = 2

class EmpleadoDetailView(LoginRequiredMixin, DetailView):
	model = Empleado

class EmpleadoCreateView(LoginRequiredMixin, CreateView):
	model = Empleado
	fields = ['clave_empleado', 'nombre', 'primer_apellido', 'segundo_apellido', 'edad', 'area', 'puesto']

class EmpleadoUpdateView(LoginRequiredMixin, UpdateView):
	model = Empleado
	fields = ['clave_empleado', 'nombre', 'primer_apellido', 'segundo_apellido', 'edad', 'area', 'puesto']
	
class EmpleadoDeleteView(LoginRequiredMixin, DeleteView):
	model = Empleado
	success_url = '/empleado'	

@login_required
def Search(request):
	query = request.GET.get('q')
	
	items = Empleado.objects.filter(Q(clave_empleado__icontains=query) | Q(nombre__icontains=query) | Q(primer_apellido__icontains=query) | Q(segundo_apellido__icontains=query)).order_by('-fecha_registro')
	items = Nomina.objects.filter(Q(empleado__nombre__icontains=query) | Q(salario_base__icontains=query) | Q(dias_laborados__icontains=query) | Q(salario_total__icontains=query)).order_by('-fecha')

	context = {
		'items': items,
		'items': items,
		
	}

	return render(request, 'empleados/search.html', context)



