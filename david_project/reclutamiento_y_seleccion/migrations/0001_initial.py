# Generated by Django 4.2.3 on 2023-07-25 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=200)),
                ('puesto_deseado', models.CharField(max_length=100)),
                ('experiencia', models.TextField()),
                ('educacion', models.TextField()),
                ('curriculum', models.FileField(null=True, upload_to='curriculums/')),
            ],
        ),
        migrations.CreateModel(
            name='Vacante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('requisitos', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudEmpleo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_solicitud', models.DateField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En Proceso'), ('rechazado', 'Rechazado'), ('contratado', 'Contratado')], max_length=100)),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reclutamiento_y_seleccion.candidato')),
                ('vacante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reclutamiento_y_seleccion.vacante')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reclutamiento_y_seleccion.candidato')),
            ],
        ),
        migrations.CreateModel(
            name='Entrevista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_entrevista', models.DateTimeField()),
                ('entrevistador', models.CharField(max_length=100)),
                ('comentario', models.TextField()),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reclutamiento_y_seleccion.solicitudempleo')),
            ],
        ),
        migrations.CreateModel(
            name='Criterio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('puntuacion', models.IntegerField()),
                ('evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reclutamiento_y_seleccion.evaluacion')),
            ],
        ),
    ]
