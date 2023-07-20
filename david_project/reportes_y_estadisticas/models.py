from django.db import models
from empleado.models import Empleado

class EvaluacionDesempenio(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    puntuacion = models.PositiveIntegerField()
    comentario = models.TextField()
    # Otros campos relevantes para la evaluación de desempeño
    
    def __str__(self):
        return f'Evaluación de {self.empleado} - {self.fecha}'
