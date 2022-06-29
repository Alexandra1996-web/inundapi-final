from django.shortcuts import render, HttpResponse
from api.models import Estaciones, Hidrometricas,Precipitaciones
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from api.serializer import PrecipitacionesSerializer
from api.serializer import HidrometricasSerializer
from api.serializer import EstacionesSerializer
# Create your views here.




#------------------------------ descargar datos de api a base de datos-----------
def home(request):
    todas = Estaciones.objects.all()
    enca = todas.get(id=100)
    hola = "que tal"
    contexto = {
        "saludo": hola,
        "esta": todas,
        "encarnacion": enca,
    }
    return render(request, "home.html", contexto)


def estacion(request):
    
    id_esta = request.GET.get('id_esta')
    print("=====", id_esta)
    esta = Estaciones.objects.get(id=id_esta)

    contexto = {
        "estacion" : esta
    }
    return render(request, "estacion.html", contexto)

def obtener_hidro(request):
    #url = f'https://hidroinformatica.itaipu.gov.py/services/hidrometricaestacion/{fecha}/{fechasig}/{estacion}/' #API datos hidrometricos
    url = f'https://hidroinformatica.itaipu.gov.py/services/hidrometricaestacion/2020-01-01/2022-06-28/12/' #API datos hidrometricos
    
    respuesta = requests.get(url)
    respuesta_json  = respuesta.json()
    print(respuesta_json)
    for medicion in respuesta_json:
        fecha_medicion = medicion.get('fecha')
        nivel_medicion = medicion.get('nivel')
        nuevo_registro = Hidrometricas()
        nuevo_registro.fecha = fecha_medicion
        nuevo_registro.nivel = nivel_medicion
        nuevo_registro.save()
    
    contexto = {
        "estacion" : respuesta_json
    }
    return render(request, "estacion.html", contexto)

def obtener_estacion(request):
    #url = f'https://hidroinformatica.itaipu.gov.py/services/hidrometricaestacion/{fecha}/{fechasig}/{estacion}/' #API datos hidrometricos
    url = f'https://hidroinformatica.itaipu.gov.py//services/estaciones/' #API datos hidrometricos
    
    respuesta = requests.get(url)
    respuesta_json  = respuesta.json()
    print(respuesta_json)
    for medicion in respuesta_json:
        fecha_medicion = medicion.get('id')
        nivel_medicion = medicion.get('nombre')
        nuevo_registro = Estaciones()
        nuevo_registro.id = fecha_medicion
        nuevo_registro.nombre = nivel_medicion
        nuevo_registro.save()
    
    contexto = {
        "estacion" : respuesta_json
    }
    return render(request, "estacion.html", contexto)




#----------------Configurar endpoints-----------------------------------

#precipitaciones

@csrf_exempt
def lista_de_precipitaciones(request):
    '''listado total de precipitaciones'''
    if request.method =='GET':
        precipitaciones_all = Precipitaciones.objects.all()
        serializer = PrecipitacionesSerializer(precipitaciones_all,many=True)
        return JsonResponse(serializer.data, safe=False)

#Hidrometricas

@csrf_exempt
def lista_de_hidrometricas(request):
    '''listado total de hidrometricas'''
    if request.method =='GET':
        hidrometricas_all = Hidrometricas.objects.all()
        serializer = HidrometricasSerializer(hidrometricas_all,many=True)
        return JsonResponse(serializer.data,safe=False)

#Estaciones
@csrf_exempt
def lista_de_estaciones(request):
    '''listado total de estaciones'''
    if request.method =='GET':
        estaciones_all = Estaciones.objects.all()
        serializer = EstacionesSerializer(estaciones_all,many=True)
        return JsonResponse(serializer.data,safe=False)