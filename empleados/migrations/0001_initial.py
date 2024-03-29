# Generated by Django 2.1.7 on 2019-03-09 03:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave_empleado', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=200)),
                ('primer_apellido', models.CharField(max_length=200)),
                ('segundo_apellido', models.CharField(max_length=200)),
                ('edad', models.IntegerField()),
                ('area', models.CharField(choices=[('Administracion', 'Administracion'), ('Aduanas', 'Aduanas'), ('Negocios', 'Negocios'), ('Mercadotecnia', 'Mercadotecnia'), ('Relaciones Publicas', 'Relaciones Publicas'), ('Mantenimiento', 'Mantenimiento'), ('Ingenieria', 'Ingenieria'), ('Diseño', 'Diseño')], default='Administracion', max_length=100)),
                ('puesto', models.CharField(choices=[('Documentador', 'Documentador'), ('Import-Export', 'Import-Export'), ('Vendedor', 'Vendedor'), ('Social Manager', 'Social Manager'), ('RP', 'RP'), ('Control de Higiene', 'Control de Higiene'), ('Produccion', 'Produccion'), ('Imagen Corporativa', 'Imagen Corporativa')], default='Documentador', max_length=100)),
                ('fecha_registro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Nomina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salario_base', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('dias_laborados', models.IntegerField(default=0)),
                ('salario_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.Empleado')),
            ],
        ),
    ]
