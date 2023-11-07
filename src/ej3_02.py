"""
Ejercicio 2.3.2

Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

def pedirEnteroPositivo(msj: str) -> int:
    num = None

    while num is None:
        try:
            num = int(input(msj))
            if num < 0:
                print("No puede ser negativo. Introduce numero valido: ")
                num = None
            else:
                return num
        except ValueError:
            print("ERROR - Introduce numero valido: ")

def numImpares(num):
    listaNumeros = ''

    for i in range(1, num):
        if i % 2 == 0:
            listaNumeros = listaNumeros + ", ".join(str(i))

    return listaNumeros

def main():
    # Pedir entero positivo por consola
    num = pedirEnteroPositivo("Introduce un numero entero positivo: ")

    # Obtener numeros impares desde el 1 hasta num
    listaNumeros = numImpares(num)

    print(f"Lista numeros impares desde 1 hasta {num}: " + listaNumeros)

if __name__ == "__main__":
    main()