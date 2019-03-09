from django.urls import path
from .views import (
	NominaListView, NominaCreateView, 
	NominaDetailView, NominaUpdateView, NominaDeleteView, NominaSearchView,
	EmpleadoListView, EmpleadoCreateView, EmpleadoDetailView,
	EmpleadoUpdateView, EmpleadoDeleteView, Search, Home
	)

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', Home, name='home'),
  	path('nomina/', NominaListView.as_view(), name='index'),
  	path('nomina/crear/', NominaCreateView.as_view(), name='nomina-crear'),
  	path('nomina/<int:pk>/', NominaDetailView.as_view(), name='nomina-detalles'),
  	path('nomina/editar/<int:pk>/', NominaUpdateView.as_view(), name='nomina-editar'),
  	path('nomina/editar/<int:pk>/', NominaUpdateView.as_view(), name='nomina-editar'),
  	path('nomina/eliminar/<int:pk>/', NominaDeleteView.as_view(), name='nomina-eliminar'),
    path('nomina/<str:clave_empleado>/', NominaSearchView.as_view(), name='nomina-empleado'),

  	path('empleado/', EmpleadoListView.as_view(), name='index-empleados'),
  	path('empleado/crear/', EmpleadoCreateView.as_view(), name='empleado-crear'),
  	path('empleado/<int:pk>/', EmpleadoDetailView.as_view(), name='empleado-detalles'),
  	path('empleado/editar/<int:pk>/', EmpleadoUpdateView.as_view(), name='empleado-editar'),
  	path('empleado/eliminar/<int:pk>/', EmpleadoDeleteView.as_view(), name='empleado-eliminar'),

    path('busqueda/', Search, name='search'),

    path('login/', auth_views.LoginView.as_view(template_name='empleados/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='empleados/logout.html'), name='logout'),



]