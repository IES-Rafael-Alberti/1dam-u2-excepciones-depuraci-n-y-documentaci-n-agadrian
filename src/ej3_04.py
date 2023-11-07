"""
Ejercicio 2.3.4

Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.
"""


def pedirEntero(msj: str) -> int:
    num = None

    try:
        num = int(input(msj))

    except Exception as e :
        print("La entrada no es correcta. Error producido: ") 
        print(e)
        


def main():
    num = pedirEntero("Introduce un numero entero: ")
    



if __name__ == "__main__":
    main()