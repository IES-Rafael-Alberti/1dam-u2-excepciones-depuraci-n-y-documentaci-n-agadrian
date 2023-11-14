import pytest
from src.ej3_03 import cuentaAtras, pedirEnteroPositivo

@pytest.mark.parametrize(
    "num, expected",
    [
        (5, "5, 4, 3, 2, 1, 0"),
        (2, "2, 1, 0"),
        (0, "0")
    ]
)
def test_cuentaAtras(num, expected):
    assert cuentaAtras(num) == expected


