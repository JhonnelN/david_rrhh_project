from django.db import models



class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre}'

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    cedula = models.PositiveIntegerField(null=True, blank=True)
    direccion = models.CharField(max_length=200)
    puesto = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_contratacion = models.DateField()
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True)
    # Otros campos relevantes para el empleado
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Solicitud(models.Model):
    TIPO_CHOICES = (
        ('vacaciones', 'Vacaciones'),
        ('reposo_medico', 'Reposo Médico'),
    )

    ESTADO_CHOICES = (
        ('espera', 'En espera'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
    )

    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=25, choices=TIPO_CHOICES)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    inicio_permiso = models.DateField()
    final_permiso = models.DateField()
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='espera')
    
    class Meta:
        verbose_name = "Solicitud"
        verbose_name_plural = "Solicitudes"
    
    def __str__(self):
        return f'{self.tipo} - {self.estado}'
