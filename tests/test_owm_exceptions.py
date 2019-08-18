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
from tarea01.sow import *
from tarea01.owm_exceptions import *


def test_invalid_location_error():
    """
    Prueba para ver que al pasarle coordenadas
    incorrectas al método correspondiente (get_weather()),
    éste lance una excepción InvalidLocationError del
    módulo owm_exceptions.
    """

    # Sintaxis: validar_coordenadas('latitud', 'longitud')
    with pytest.raises(InvalidLocationError):
        validar_coordenadas('-5a', '4.b') # Ambas coordenadas incorrectas.
        validar_coordenadas('95.6', 'N') # Longitud incorrecta.
        validar_coordenadas('56.lat', '567.2') # Latitud incorrecta.
