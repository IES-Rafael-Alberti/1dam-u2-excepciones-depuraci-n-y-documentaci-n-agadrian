"""
Ejercicio 2.3.4

Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.
"""


def comprobarEntero(numero: str) -> int:
    """
    Transforma si es posible a int

    Args:
        numero (str): valor a convertir a int
    
    Retorna:
        int:
            el valor transformado a int
            None si no se ha podido transformar
    """

    num = int(numero)

    return num


def main():
    numero = input("Introduce un numero entero: ")

    try:    
        comprobarEntero(numero)
    except ValueError as e:
        print("La entrada no es correcta: " + str(e))



if __name__ == "__main__":
    main()