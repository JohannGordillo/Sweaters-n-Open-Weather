# -*- coding: utf-8 -*-

"""
====================================================
Autor: Johann Gordillo
Email: jgordillo@ciencias.unam.mx
====================================================
El programa recibe un archivo .CSV ingresado
por el usuario por medio de un manejador de
archivos con las ciudades, y sus respectivas
coordenadas geográficas, para que el programa
devuelva la temperatura en tiempo real de las mismas
haciendo uso del web service Open Weather Map,
al que se le realizan peticiones de información
sobre el clima dandole coordenadas geográficas.
====================================================
"""


from tarea01.files_gui import FileBrowser
from tarea01.owm_exceptions import *
import configparser
import threading
import requests
import csv


def get_api_key():
    """
    Regresa la llave de la API para poder hacer peticiones
    al servicio web.
    """

    config = configparser.ConfigParser()
    config.read('./data/config.ini')
    return config['openweathermap']['api']


def validar_coordenadas(lat, lon):
    """
    Valida que la latitud y longitud dadas sean valores
    numéricos. Si no lo son, lanza una excepción.
    """

    try:
        eval(lat)
        eval(lon)
    except Exception:
        raise InvalidLocationError


def get_weather(api_key, lat, lon):
    """
    Regresa la información detallada sobre el clima en la ubicación con
    coordenadas latitud 'lat' y longitud 'lon' en un formato JSON.
    """

    # Checamos que las coordenadas sean válidas.
    validar_coordenadas(lat, lon)

    # Dirección a la que haremos las peticiones.
    params = f"lat={lat}&lon={lon}&units=metric&appid={api_key}"
    url = f"https://api.openweathermap.org/data/2.5/weather?{params}"

    # Intentamos obtener la información del servidor de Open Weather Map.
    try:
        r = requests.get(url, timeout=8)
        return r.json()

    except requests.exceptions.ConnectionError:
        print("Error\nHa ocurrido un error al intentar conectarse con el servidor de Open Weather Map. Lo sentimos.")
        raise SystemExit

    except requests.exceptions.ConnectTimeout:
        print("Error\nEl servidor ha tardado demasiado tiempo en establecer una conexión.")
        raise SystemExit

    except requests.exceptions.ReadTimeout:
        print("Error\nEl servidor ha tardado demasiado tiempo en responder a las peticiones. Lo sentimos.")
        raise SystemExit

    except requests.exceptions.InvalidSchema:
        print(f"Error\nNo se encontraron adaptadores de conexión para:\n{url}")
        raise SystemExit


def main():
    """
    Función principal.
    """

    cache = {} # {
               #    NOMBRE_CIUDAD1: {
               #                        lat =  x,
               #                        lon =  y,
               #                        temp = z
               #                    },
               #    NOMBRE_CIUDAD2: { ... },
               #    ...
               # }

    # Obtenemos la llave de la API.
    api_key = get_api_key()

    # Desplegamos una interfaz gráfica para buscar el archivo .CSV.
    fb = FileBrowser()
    fb.search_path()
    file_path = fb.get_path()

    # Leemos el archivo .CSV.
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            # -------------------------- CIUDAD ORIGEN --------------------------

            # Nombre de la ciudad origen.
            origen = row["origin"]

            # Si la ciudad origen ya está en el caché, regresamos su temperatura.
            if origen in cache.keys():
                temp_origen = cache[origen]["temp"]

            else:
                # Latitud y Longitud de la ciudad origen.
                lat_origen = row["origin_latitude"]
                lon_origen = row["origin_longitude"]

                # Intentamos extraer la información del clima en la ciudad origen.
                try:
                    info_origen = get_weather(api_key, lat_origen, lon_origen)
                except InvalidLocationError:
                    print("Error\nCoordenadas inválidas.")
                    raise SystemExit

                # Obtenemos la temperatura actual en la ciudad origen.
                temp_origen = info_origen["main"]["temp"]

                # Agregamos al caché su información.
                cache[origen] = {"lat": lat_origen,
                                 "lon": lon_origen,
                                 "temp": temp_origen}

            # -------------------------------------------------------------------

            # -------------------------- CIUDAD DESTINO -------------------------

            # Nombre de la ciudad destino.
            destino = row["destination"]

            # Si el destino ya está en el caché, regresamos su temperatura.
            if destino in cache.keys():
                temp_destino = cache[destino]["temp"]

            else:
                # Latitud y Longitud de la ciudad destino.
                lat_destino = row["destination_latitude"]
                lon_destino = row["destination_longitude"]

                # Intentamos extraer la información del clima en la ciudad destino.
                try:
                    info_destino = get_weather(api_key, lat_destino, lon_destino)
                except InvalidLocationError:
                    print("Error\nCoordenadas inválidas.")
                    raise SystemExit

                # Temperatura actual en la ciudad destino.
                temp_destino = info_destino["main"]["temp"]

                # Lo agregamos al caché.
                cache[destino] = {"lat": lat_destino,
                                 "lon": lon_destino,
                                 "temp": temp_destino}

            # -------------------------------------------------------------------

            # Imprimimos las temperaturas en consola.
            print(f"\nTemperatura en la ciudad origen [{origen}]: {temp_origen} °C\n")
            print(f"Temperatura en la ciudad destino [{destino}]: {temp_destino} °C\n")
