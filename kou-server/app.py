from cgitb import html
from flask import Flask, jsonify, render_template
import sqlite3
import requests
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

# CREATE TABLE "precipitaciones" (
# 	"id"	INTEGER NOT NULL,
# 	"fecha"	TEXT NOT NULL,
# 	"mmh"	REAL NOT NULL DEFAULT 0.0,
# 	PRIMARY KEY("id")
# );

def informacion_requerida_precipitaciones():
# acá van las apis

    url= 'https://hidroinformatica.itaipu.gov.py//services/precipitacionestacion/2016-11-01/2016-11-28/12/' 
    respuesta = requests.get(url)
    respuesta_json = respuesta.json()
    return respuesta_json

# acá se conecta con la ruta de la página.
@app.route('/precipitaciones')
def precipitaciones():
    info = informacion_requerida_precipitaciones()
    print(type(info))
    print(len(info))
    print(info[0])
    print(info[0]['fecha'])
    print(info[0].get('fecha'))
    ###################################
    con= sqlite3.connect('../db.sqlite3')
    repe =0
    cur = con.cursor()
    for medicion in info:
        #print(medicion.get('fecha'), medicion.get('mmh'))
        id = medicion.get('id')
        fecha =medicion['fecha']
        mmh  = medicion['mmh']
        print(id,fecha,mmh)
        #("id",  "fecha", "mmh")
        try:
            cur.execute('INSERT INTO api_precipitaciones VALUES (?, ?, ?)', (int(id), fecha, mmh))
        except Exception as e:
            repe = repe+1

    con.commit()
    con.close()


    ##################################
    canti = len(info)
    return render_template ("precipitaciones.html", cantidad=canti,repetidos=repe)

def informacion_requerida_hidrometrica():
# acá van las apis

    url= 'https://hidroinformatica.itaipu.gov.py//services/hidrometricaestacion/2016-11-01/2016-11-28/12/' 
    respuesta = requests.get(url)
    respuesta_json = respuesta.json()
    return respuesta_json

# acá se conecta con la ruta de la página.
@app.route('/hidrometrica')
def hidrometrica():
    info = informacion_requerida_hidrometrica()
    print(type(info))
    print(len(info))
    print(info[0])
    print(info[0]['fecha'])
    ###################################
    con= sqlite3.connect('../db.sqlite3')
    repe =0
    cur = con.cursor()
    for medicion in info:
        #print(medicion.get('fecha'), medicion.get('mmh'))
        id = None
        nivel = medicion['nivel']
        fecha = medicion['fecha']
        
        print(nivel,fecha)
        #("nivel",  "fecha")
        try:
            cur.execute('INSERT INTO api_hidrometricas VALUES (?, ?, ?)', (id, fecha, nivel))
        except Exception as e:
            repe = repe+1
            print(e)
            print("no entra la consulta nde plaga")
            print(f"Nivel: {type(nivel)}")
            print(f"Fecha: {type(fecha)}")


    con.commit()
    con.close()


    ##################################
    canti = len(info)
    return render_template ("hidrometricas.html", cantidad=canti,repetidos=repe )




