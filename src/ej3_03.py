"""
Ejercicio 2.3.3

Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto.
"""


def pedirEnteroPositivo(msj: str) -> int:
    """
    Pide un numero por consola hasta que es valido (entero positivo)

    Args:
        msj (str): mensaje a mostrar en el input que pide el numero

    Retorna:
        int: del numero introducido
    """

    num = None

    # Si es < 0, lanza error y vuelve a preguntar
    while num is None or num < 0:
        try:
            num = int(input(msj))
            if num < 0:
                raise ValueError
            
        except ValueError:
            msj = "ERROR - Introduce numero validoo: "
    
    return num



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