"""
Ejercicio 2.3.3

Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto.
"""

from ej3_02 import pedirEnteroPositivo


def cuentaAtras(num: int):
    """
    Almacena en variable numeros de 1 en 1, desde (num) hasta 0

    Args:
        num (int): numero introducido inicio cuenta atras
    
    Retorna:
        str: lista de numeros cuenta atras
    """
    listaNumeros = ''

    # desde num hasta 0, cada -1
    for i in range(num, -1, -1):
        #Evita añadir coma antes del primer caracter, empieza en el segundo
        if i < num:
            listaNumeros += ", "
        listaNumeros += str(i)
    
    return listaNumeros


def main():
    # Pedir numero entero positivo
    num = pedirEnteroPositivo("Introduce un numero entero positivo: ")

    # Asignar cuenta atras
    listaNumeros = cuentaAtras(num)

    print("Cuenta atras: " + listaNumeros)

if __name__ == "__main__":
    main()