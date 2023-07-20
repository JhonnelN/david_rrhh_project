# Generated by Django 4.2.3 on 2023-07-14 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('vacaciones', 'Vacaciones'), ('reposo_medico', 'Reposo Médico'), ('permiso_extraordinario', 'Permiso Extraordinario')], max_length=25)),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True)),
                ('inicio_permiso', models.DateField()),
                ('final_permiso', models.DateField()),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('espera', 'En espera'), ('aprobado', 'Aprobado'), ('rechazado', 'Rechazado')], default='espera', max_length=20)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.empleado')),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='empleado.departamento'),
        ),
    ]