from django.db import models

class Candidato(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    puesto_deseado = models.CharField(max_length=100)
    experiencia = models.TextField()
    educacion = models.TextField()
    # Otros campos relevantes para el candidato
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Vacante(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    requisitos = models.TextField()
    # Otros campos relevantes para la vacante
    
    def __str__(self):
        return self.titulo

class SolicitudEmpleo(models.Model):
    # Opciones
    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('rechazado', 'Rechazado'),
        ('contratado', 'Contratado')
    )
    # Modelos
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE)
    fecha_solicitud = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=100, choices=ESTADO_CHOICES)
    # Otros campos relevantes para la solicitud de empleo
    
    def __str__(self):
        return f'{self.candidato} - {self.vacante}'


class Entrevista(models.Model):
    solicitud = models.ForeignKey(SolicitudEmpleo, on_delete=models.CASCADE)
    fecha_entrevista = models.DateTimeField()
    entrevistador = models.CharField(max_length=100)
    comentario = models.TextField()
    # Otros campos relevantes para la entrevista
    
    def __str__(self):
        return f'Entrevista para {self.solicitud} - {self.fecha_entrevista}'

class Evaluacion(models.Model):
    candidato = models.ForeignKey('Candidato', on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

class Criterio(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    puntuacion = models.IntegerField()