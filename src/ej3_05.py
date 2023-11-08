"""
Ejercicio 2.3.5

Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"
"""

def comprobarContraseña(contraseña1:str, contraseña2:str) -> bool:
    """
    Comprueba si las contraseñas coinciden, si no lanza excepcion NameError

    Args:
        contraseña1: str 
        contraseña2: str
    """
    
    if contraseña1 != contraseña2:
        raise NameError
    
   

def main():
    try:
        contraseña1 = "contraseña123"
        contraseña2 = input("Introduce contraseña: ")
        comprobarContraseña(contraseña1,contraseña2)
        print("Coinciden")
    except NameError:
        print("Incorrect Password!!")


if __name__ == "__main__":
    main()