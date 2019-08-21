import pytest
import tarea01.snow

FILE_PATH = "./data/1.csv"

def main(file):
    """
    Llama a la función principal
    del módulo snow.
    """
    tarea01.snow.main(file)
    return 0

def test_weathers():
    assert main(FILE_PATH) == 0
