# -*- coding: utf-8 -*-

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
import time
import threading


def select_files():
    fb = FileBrowser()
    fb.search_paths()
    return fb.get_paths()

def main(file):
    tarea01.snow.main(file)

if __name__ == '__main__':
    files = select_files()
    ti = time.time()
    num_threads = len(files)
    threads = []

    for i in range(num_threads):
        process = threading.Thread(target=main, \
                                    args=(files[i],))
        process.start()
        threads.append(process)
        time.sleep(5)

    for th in threads:
        th.join()
    tf = time.time()
    print("Ejecución finalizada en {:.2f} segundos.".format(tf-ti))
