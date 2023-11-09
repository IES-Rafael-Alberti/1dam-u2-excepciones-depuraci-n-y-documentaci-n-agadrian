#### ALGORITMO BURBUJA ####

# BULCE PADRE HACE LAS PASADAS range (0, len(lista)) 
#BUCLE HIJO HACE una pasada menos del total de elementos de la lista (0, len(lista) - 1)
"""
LISTA = ..........
lsitaOrdenada = ordenarlista(lista)
obtenerListaNumeros (listaOrdenada)
print(obtenerListaNumeros)
"""


def ordenarLista(lista):
    # Bucle padre e hijo se repetira 1 vez menos del total de numeros en la lista
    for i in range(0, len(lista)-1):
        for j in range(0, len(lista)-1):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista

def main():
    lista = [1,8,6,2,9,3,10,7]
    listaOrdenada = ordenarLista(lista)

    print(listaOrdenada)

if __name__ == "__main__":
    main()
