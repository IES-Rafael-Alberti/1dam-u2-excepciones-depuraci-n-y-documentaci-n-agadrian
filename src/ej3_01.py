'''
Ejercicio 2.3.1
    Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''

def mostrarAños(edad):
    for i in range(1, edad+1):
        print(i)
    if edad <= 0:
        raise ValueError ("La edad debe ser mayor a 0")
    

def main():
    try:
        edad = int(input("Introduce edad: "))
        mostrarAños(edad)
    except:
        print("Debes introducir un numero")



if __name__ == "__main__":
    main()