#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
====================================================
Autor: Johann Gordillo
Email: jgordillo@ciencias.unam.mx
====================================================
El modulo contiene pruebas para el módulo
files_gui.
====================================================
"""

import pytest
import requests
from tarea01.snow import *


API_KEY = get_api_key()

def test_connection_error():
    """
    Probamos que al intentar conectarse al servidor de
    Open Weather Map con un timeout extremadamente pequeño
    (para casos de la prueba, unicamente), se lance una
    excepción, pues la conexión no ha sido lo
    suficientemente 'rápida'.
    En el código original el timeout es de 8 segundos.
    """

    # Valores válidos para latitud y longitud
    lat = '57'
    lon = '432'

    # URL con parámetros correctos.
    params = f"lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
    url = f"https://api.openweathermap.org/data/2.5/weather?{params}"

    with pytest.raises(requests.exceptions.ConnectionError):
        # Timeout extremandamente pequeño,
        # unicamente para comprobar que la excepcion
        # sea lanzada.
        r = requests.get(url, timeout=0.0000001)


def test_invalid_schema_error():
    # Valores válidos para latitud y longitud
    lat = '57'
    lon = '432'

    # Parametros correctos.
    params = f"lat={lat}&lon={lon}&units=metric&appid={API_KEY}"

    # Pasemos una URL inválida, en la que en lugar
    # de usar el protocolo https, usamos htps (que
    # además no existe).
    url = f"htps://api.openweathermap.org/data/2.5/weather?{params}"

    with pytest.raises(requests.exceptions.InvalidSchema):
        r = requests.get(url, timeout=8)
