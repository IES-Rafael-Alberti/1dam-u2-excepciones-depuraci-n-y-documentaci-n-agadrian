import pytest
from src.ej3_04 import comprobarEntero

@pytest.mark.parametrize(
    "numero, expected",
    [
        ("5", 5),
        ("-5", -5),
        ("0", 0),
        ("55", 55),
        ("-600", -600)
    ]
)
def test_comprobarEntero(numero, expected):
    assert comprobarEntero(numero) == expected


