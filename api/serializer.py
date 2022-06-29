
from rest_framework import serializers
from api.models import Precipitaciones
from api.models import Hidrometricas
from api.models import Estaciones


class PrecipitacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precipitaciones
        fields = ['id','fecha','mmh']

class HidrometricasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hidrometricas
        fields = ['fecha','nivel']

class EstacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estaciones
        fields = ['id','nombre']

