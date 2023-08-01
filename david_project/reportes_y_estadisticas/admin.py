from django.contrib import admin
from .models import (
    EvaluacionDesempenio, RetrasoEmpleado, 
    AsignacionUniforme, Uniforme, 
    AmonestacionEmpleado, HoraExtra
    )

admin.site.register(EvaluacionDesempenio)
admin.site.register(RetrasoEmpleado)
admin.site.register(AsignacionUniforme)
admin.site.register(Uniforme)
admin.site.register(AmonestacionEmpleado)
admin.site.register(HoraExtra)



