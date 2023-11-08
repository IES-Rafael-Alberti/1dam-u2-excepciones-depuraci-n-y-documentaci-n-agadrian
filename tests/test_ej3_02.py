import pytest
from src.ej3_02 import comprobarEnteroPositivo, numImpares

@pytest.mark.parametrize(
    "entrada, expected",
    [
        ("5",5),
        ("26",26),
        ("125",125)
       
    ]
)
def test_comprobarEnteroPositivo(entrada, expected):
    assert comprobarEnteroPositivo(entrada) == expected



@pytest.mark.parametrize(
    "num, expected",
    [
        (5,"1, 3, 5"),
        (9,"1, 3, 5, 7, 9"),
        (0, ""),
        (1,"1")
    ]
)
def test_numImpares(num, expected):
    assert numImpares(num) == expected



def test_comprobarEnteroPositivo_ValueError():
    with pytest.raises(ValueError):
        comprobarEnteroPositivo("-5")

def test_comprobarEnteroPositivo_ValueError2():
    with pytest.raises(ValueError):
        comprobarEnteroPositivo("cinco")

def test_comprobarEnteroPositivo_ValueError3():
    with pytest.raises(ValueError):
        comprobarEnteroPositivo(-45)