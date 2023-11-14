'''
Ejercicio 2.3.1
    Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''

def pedirEdad(msj: str) -> int:
    """
    Solicita la edad hasta que sea valida

    Args:
        msj (str): mensaje mostrado para pedir edad
        
    Retorna:
        int: la edad introducida
    """
    edad = None

    while edad is None:
        try:
            edad = int(input(msj))
            if edad <= 0 or edad > 125:
                print("Error, debe introducir una edad valida: ")
                edad = None
            else:
                return edad
            
        except ValueError:
            print("Error, debe introducir una edad valida ")



def mostrarAños(edad: int):
    """
    Almacena todos los numeros desde el 1, de 1 en 1 hata la edad introducida

    Args:
        edad (int): edad que introduce por consola
    Retorna:
        listaEdades (str): numeros del 1-edad cada uno en una nueva linea
        
    """
    listaEdades = ''

    for i in range(1, edad+1):
        listaEdades += str(i) + "\n"
    
    return listaEdades



def main():
    #Pedir edad
    edad = pedirEdad("Introduce edad: ")

    #Mostrar numero 1 hasta edad
    listaNumeros = mostrarAños(edad)

    print("Años cumplidos: \n" + listaNumeros)


if __name__ == "__main__":
    main()