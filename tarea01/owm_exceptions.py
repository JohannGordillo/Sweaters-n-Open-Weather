# -*- coding: utf-8 -*-

"""
====================================================
Autor: Johann Gordillo
Email: jgordillo@ciencias.unam.mx
====================================================
Excepciones personalizadas para el programa.
====================================================
"""


class InvalidLocationError(Exception):
    """
    Error lanzado cuando las coordenadas de una
    localización proporcionadas al programa son
    incorrectas.
    """
    pass


class SaturatedServerError(Exception):
    """
    Error lanzado cuando el servidor que proporciona
    el servicio web se encuentra saturado por
    excesivas peticiones.
    """
    pass
