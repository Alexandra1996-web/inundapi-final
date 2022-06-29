"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import home, estacion, obtener_estacion, obtener_hidro,lista_de_precipitaciones,lista_de_hidrometricas,lista_de_estaciones

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    #path('estacion/', estacion),
    #path('hidro/', obtener_hidro),
    #path('estaciones/', obtener_estacion),
    path('precipitaciones/',lista_de_precipitaciones ),
    path('hidrometricas/', lista_de_hidrometricas),
    path('listaestaciones/', lista_de_estaciones),

]
