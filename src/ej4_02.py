#### ALGORITMO BURBUJA ####

def ordenarLista(lista) -> list:
    """
    Ordena una lista numerica de menor a mayor

    Args:
        list: lista numerica desordenada

    Retorna:
        list: ordenada de menor a mayor
    """
    # Bucle padre e hijo se repetira 1 vez menos del total de numeros en la lista
    for i in range(0, len(lista) - 1):
        for j in range(0, len(lista) - 1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
    return lista


def obtenerListaNumeros(lista):
    """
    Almacena en una variable, los numeros de forma mas legible, separados por comas

    Args:
        list: lista ordenada
    
    Retorna:
        str: numeros de la ordenados seprados por coma 
    """
    ordenado = " "

    for i in lista:
        if i == lista[-1]:
            ordenado += str(i)
        else:
            ordenado += str(i) + ", "
    
    return ordenado


def main():
    lista = [1,8,6,4,45,23,56,34,34]
    listaOrdenada = ordenarLista(lista)
    listaFormateada = (obtenerListaNumeros(listaOrdenada))

    print(f"Lista final: {listaFormateada}")



if __name__ == "__main__":
    main()
