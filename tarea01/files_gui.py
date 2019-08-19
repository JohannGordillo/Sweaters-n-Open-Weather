# -*- coding: utf-8 -*-

"""
====================================================
Autor: Johann Gordillo
Email: jgordillo@ciencias.unam.mx
====================================================
El modulo contiene la clase FileBrowser que permite
mostrar una ventana con el directorio actual
y deja al usuario seleccionar de ahí el
archivo .CSV que será pasado como entrada al
programa principal.
====================================================
"""


from tkinter import *
from tkinter import filedialog as fd


class FileBrowser(object):
    """
    Clase para representar un manejador de archivos
    con interfaz gráfica.
    """

    def __init__(self, file_path=None):
        """
        Constructor para la clase.
        """
        self.__root = Tk()
        self.__file_path = file_path

        self.__file_paths = []

    def search_paths(self):
        if len(self.__file_paths) == 0:
            self.__root.withdraw()
            file_types = (("csv files", "*.csv"),)
            files = fd.askopenfilenames(title="Selecciona el archivo", filetypes=file_types)
            self.__file_paths = list(files)

    def get_paths(self):
        return self.__file_paths

    def search_path(self):
        """
        Despliega una ventana del manejador de archivos
        ubicada en la carpeta donde se encuentre el usuario
        para que éste seleccione el archivo .CSV con
        los vuelos.

        Da al atributo privado file_path del objeto
        el path del archivo seleccionado por el usuario.
        """
        if self.__file_path == None:
            self.__root.withdraw()
            file_types = (("csv files", "*.csv"),)
            self.__file_path = fd.askopenfilename(title="Selecciona el archivo", \
                                                  filetypes=file_types)

    def get_path(self):
        """
        Regresa el path del archivo seleccionado por el usuario.
        """
        return self.__file_path
