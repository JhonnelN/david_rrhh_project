from django.db import models
from empleado.models import Empleado, Departamento


class RetrasoEmpleado(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_retraso = models.DateField()
    descripcion = models.CharField(max_length=200)
    tiempo_retraso_minutos = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = "Retrasos de Empleado"
        verbose_name_plural = "Retrasos de Empleados"    

    def __str__(self):
        return f"Retraso de {self.empleado} - {self.fecha_retraso}"

class EvaluacionDesempenio(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    puntuacion = models.PositiveIntegerField()
    comentario = models.TextField()
    # Otros campos relevantes para la evaluación de desempeño
    
    class Meta:
        verbose_name = "Evaluacion de Desempeño"
        verbose_name_plural = "Evaluaciones de Desempeño"

    def __str__(self):
        return f'Evaluación de {self.empleado} - {self.fecha}'


class Uniforme(models.Model):
    tipo = models.CharField(max_length=100)
    # Otros campos relacionados con los uniformes, como talla, color, etc.

    def __str__(self):
        return self.tipo


class AsignacionUniforme(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    uniforme = models.ForeignKey(Uniforme, on_delete=models.CASCADE)
    cantidad_asignada = models.PositiveIntegerField(default=0)
    fecha_asignacion = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Asignación de {self.uniforme.tipo} a {self.empleado.nombre}"


class HoraExtra(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    horas_trabajadas = models.PositiveIntegerField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return f"Horas extras de {self.empleado} - {self.fecha}"


class AmonestacionEmpleado(models.Model):
    FALTA_CHOICES = [
        ('Agresión Verbal', 'Agresión Verbal'),
        ('Agresión Física', 'Agresión Física'),
        ('Acoso', 'Acoso'),
        ('Otro', 'Otro'),
        # Agrega aquí más opciones de tipo de falta si es necesario
    ]

    GRAVEDAD_CHOICES = [
        ('Leve', 'Leve'),
        ('Moderada', 'Moderada'),
        ('Grave', 'Grave'),
    ]
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    numero_control_reporte = models.AutoField(primary_key=True)
    fecha = models.DateField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    tipo_falta = models.CharField(choices=FALTA_CHOICES, max_length=50)
    gravedad = models.CharField(choices=GRAVEDAD_CHOICES, max_length=10)
    resumen = models.TextField()
    causas = models.TextField()
    comentarios = models.TextField()

    def __str__(self):
        return f"Amonestación {self.numero_control_reporte} - {self.empleado}- {self.departamento} - {self.tipo_falta} - {self.gravedad}"

