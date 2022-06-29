# INUNDAPI


DOCUMENTACIÓN PRELIMINAR DE INUNDAPI

-DESCRIPCIÓN INUNDAPI Esta API endpoit pretende dar fácil acceso a las personas o entidades encargadas de las tomas de decisiones en casos de inundación la optimización de acciones y dar a conocer los posibles usos y aplicaciones de la información condesada en la API. -OBTENCIÓN DE INFORMACIÓN La fuente de información es obtenida a partir de API endpoit de páginas con información sobre meteorología e hidrología, en la fase inicial del proyecto se tomó como fuente de información la página de Centro Internacional de Hidroinformática – CIH de la ITAIPU Binacional https://hidroinformatica.itaipu.gov.py/docs/. Para este prototipo se trabajó con las siguientes API Endpoint:

/services/hidrometricaestacion/<fecha>/<fechasig>/<estacion>/
La API endpoint de estaciones hidrométricas: retorna una lista con datos hidrométricos (Nivel (m), Conductividad (mS/cm), pH, Turbidez (NTU), Oxígendo Dis.(ppm), Temperatura (°C)) de una estacíon <estacion>, desde <fecha> hasta <fechasig>. Formato de fecha yyyy-mm-dd.

/services/meteorologicasestacion/<fecha>/<fechasig>/<estacion>/
La API endpoint de estaciones meteorológicas: retorna una lista con datos meteorologicos (mm, observacion (obs)y fecha de creacion del registro(created_at) de una estacíon <estacion>, desde <fecha> hasta <fechasig>. Formato de fecha yyyy-mm-dd. 


A continuación, se puede ver el formato en el que ingresa la información para su procesamiento considerando como fuente de información la página del Centro Internacional de Hidroinformática – CIH de la ITAIPU Binacional:


[
{
        "fecha": "2022-02-01 10:00:00 PYST",
        "nivel": -0.2,
        "conductividad": null,
        "ph": null,
        "turbidez": null,
        "od": null,
        "tempagua": null,
        "created_at": "2022-02-01 11:00:21 PYST",
        "obs": null
    },
]

Tecnologías utilizadas para el proyecto 


Insomnia
Postman
SQLite3
Flask
Sqlite sqlalchemy
Django REST
Tailwind
Autores:

-Fabiola Belén Balbuena Morínigo

-Nestor Manueal Castelnovo Acuña

-Víctor Hugo Antonio Vidovich Sarubbi

-Diana Raquel Coronel Nakagawa

-Pilar Edith Castellano Lugo

Coaches de Desarrollo: Alexandra Cáceres y Sergio García

Licencia Open Source
