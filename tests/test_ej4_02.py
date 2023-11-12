import pytest
from src.ej4_02 import ordenarLista, obtenerListaNumeros

@pytest.mark.parametrize(
    "lista, expected",
    [
        ([32,56,3,1],[1,3,32,56]),
        ([1,8,6,4,45,23,56,34,12],[1, 4, 6, 8, 12, 23, 34, 45, 56])
    ]
)
def test_ordenarLista(lista, expected):
    assert ordenarLista(lista) == expected


@pytest.mark.parametrize(
    "lista2, expected",
    [
        ([1,6,8], "1, 6, 8"),
        ([1, 4, 6, 8, 12, 23, 34, 45, 56],"1, 4, 6, 8, 12, 23, 34, 45, 56")
    ]
)
def test_obtenerListaNumeros(lista2, expected):
    assert obtenerListaNumeros(lista2) == expected