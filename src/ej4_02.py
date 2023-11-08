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
    for i in range(0, len(lista)):
        for j in range(0, len(lista)-1):
            if lista[j] > lista[j+1]:
                lista[j] == lista[j+1]
    return lista

def main():
    lista = [1,4,6,2,10]
    listaOrdenada = ordenarLista(lista)

    print(listaOrdenada)

if __name__ == "__main__":
    main()
