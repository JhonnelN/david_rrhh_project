# Generated by Django 4.2.3 on 2023-07-25 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uniforme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RetrasoEmpleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_retraso', models.DateField()),
                ('descripcion', models.CharField(max_length=200)),
                ('tiempo_retraso_minutos', models.PositiveIntegerField(default=0)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='HoraExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('horas_trabajadas', models.PositiveIntegerField()),
                ('descripcion', models.TextField()),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.departamento')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='EvaluacionDesempenio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('puntuacion', models.PositiveIntegerField()),
                ('comentario', models.TextField()),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='AsignacionUniforme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_asignada', models.PositiveIntegerField(default=0)),
                ('fecha_asignacion', models.DateField()),
                ('fecha_devolucion', models.DateField(blank=True, null=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.empleado')),
                ('uniforme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes_y_estadisticas.uniforme')),
            ],
        ),
        migrations.CreateModel(
            name='AmonestacionEmpleado',
            fields=[
                ('numero_control_reporte', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('tipo_falta', models.CharField(choices=[('Agresión Verbal', 'Agresión Verbal'), ('Agresión Física', 'Agresión Física'), ('Acoso', 'Acoso'), ('Otro', 'Otro')], max_length=50)),
                ('gravedad', models.CharField(choices=[('Leve', 'Leve'), ('Moderada', 'Moderada'), ('Grave', 'Grave')], max_length=10)),
                ('resumen', models.TextField()),
                ('causas', models.TextField()),
                ('comentarios', models.TextField()),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.departamento')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.empleado')),
            ],
        ),
    ]
