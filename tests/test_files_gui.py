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
from tarea01.files_gui import FileBrowser


def test_get_path():
    file_path = "../data/dataset.csv"
    fb = FileBrowser(file_path)
    returned_file_path = fb.get_path()
    assert file_path
