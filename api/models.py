from django.db import models
from django.utils import timezone

class Precipitaciones(models.Model):
    id = models.CharField(max_length=10,primary_key=True)#repasar primary 
    fecha = models.CharField(max_length=50)
    mmh = models.FloatField()
    
    def __str__(self):
        return f"Medicion ID⁼{self.id} - {self.fecha}"




class Hidrometricas(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.CharField(max_length=50)
    nivel = models.FloatField()

    def __str__(self):
        return f"<Hidrometrica {self.id} - Nivel {self.nivel} - {self.fecha}>"

class Estaciones(models.Model):
    id = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return f"<Estacion {self.id} - {self.nombre}>"



