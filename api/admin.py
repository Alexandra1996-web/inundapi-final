from django.contrib import admin
from .models import Precipitaciones
from .models import Hidrometricas
from .models import Estaciones



# Register your models here.

admin.site.register(Precipitaciones)
admin.site.register(Hidrometricas)
admin.site.register(Estaciones)