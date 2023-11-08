import pytest
from src.ej3_01 import mostrarAños

@pytest.mark.parametrize(
    "edad, expected",
    [
        (5,"1\n2\n3\n4\n5\n"),
        (1,"1\n")    
    ]
)
def test_mostrarAños(edad, expected):
    assert mostrarAños(edad) == expected

