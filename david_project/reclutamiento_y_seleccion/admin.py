from django.contrib import admin
from .models import Candidato, Vacante, SolicitudEmpleo, Entrevista, Evaluacion

admin.site.register(Candidato)
admin.site.register(Vacante)
admin.site.register(SolicitudEmpleo)
admin.site.register(Entrevista)
admin.site.register(Evaluacion)