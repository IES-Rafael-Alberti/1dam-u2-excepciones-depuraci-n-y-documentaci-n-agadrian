"""
Ejercicio 2.3.2

Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

def comprobarEnteroPositivo(entrada: str) -> int:
    """
    Pide un numero por consola hasta que es valido (entero positivo)

    Args:
        msj (str): mensaje a mostrar en el input que pide el numero

    Retorna:
        int: del numero introducido
    """
    num = int(entrada)

    if num < 0:
        raise ValueError("**Error** número negativo.")
    
    return num


def numImpares(num:int) -> str:
    """
    Calcula y almacena los numeros impares entre el 1 y el numero pasado como argumento (num)

    Args:
        num (int): numero limite del rango

    Retorna:
        str: cadena de texto de los numeros impares entre 1 - num
    """

    listaNumeros = ''

    for i in range(1, num+1):
        if i % 2 != 0:
            # Separar por comas, excepto la primera vez
            if i > 1:
                listaNumeros += ", "
            listaNumeros += str(i)

    return listaNumeros


def main():
    num = None

    while num is None or num < 0:
        entrada = input("Introduce un numero entero positivo: ")
        try:
            num = comprobarEnteroPositivo(entrada)
        except ValueError as e:
            print("ERROR - " + str(e))
        except Exception as e:
            print("ERROR - " + str(e))

    # Obtener numeros impares desde el 1 hasta num
    listaNumeros = numImpares(num)

    print(f"Lista numeros impares desde 1 hasta {num}: " + listaNumeros)


if __name__ == "__main__":
    main()