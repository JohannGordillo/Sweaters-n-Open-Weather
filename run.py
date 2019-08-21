# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
====================================================
Autor: Johann Gordillo
Email: jgordillo@ciencias.unam.mx
====================================================
Ejecución del programa principal usando hilos.
====================================================
"""

import tarea01.snow
from tarea01.files_gui import FileBrowser
import threading


def select_files():
    """
    Permite al usuario seleccionar los archivos
    con ayuda de una interfaz gráfica.

    Regresa una lista con las rutas a los archivos.
    """
    fb = FileBrowser()
    fb.search_paths()
    return fb.get_paths()


def main(file):
    """
    Llama a la función principal
    del módulo snow.
    """
    tarea01.snow.main(file)


if __name__ == '__main__':
    # Permitimos al usuario seleccionar los archivos.
    files = select_files()

    # Trabajamos con un hilo por archivo.
    num_threads = len(files)

    # Lista de hilos.
    threads = []

    for i in range(num_threads):
        process = threading.Thread(target=main, args=(files[i],))
        process.start()
        threads.append(process)

    for th in threads:
        th.join()
