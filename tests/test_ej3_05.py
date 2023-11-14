import pytest
from src.ej3_05 import comprobarContraseña




def test_comprobarContraseña_NameError():
    with pytest.raises(NameError):
        comprobarContraseña("pedro", "antonio")

def test_comprobarContraseña_NameError2():
    with pytest.raises(NameError):
        comprobarContraseña("456", "4556")