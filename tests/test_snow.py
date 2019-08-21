#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
====================================================
Autor: Johann Gordillo
Email: jgordillo@ciencias.unam.mx
====================================================
El modulo contiene pruebas para el módulo
principal del programa.
====================================================
"""

import pytest
import requests
import tarea01.snow


FILE_PATH = "./data/1.csv"

def main(file):
    """
    Llama a la función principal
    del módulo snow.
    """
    try:
        tarea01.snow.main(file)
        return 0
    except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout):
        return -1


def test_snow():
    """
    Pasa la prueba si el programa se ejecuta
    sin problemas, o si el problema se debe a
    un error en la conexión y no depende del
    programa.
    """
    res = main(FILE_PATH)
    assert res == 0 or res == -1
