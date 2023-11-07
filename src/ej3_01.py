'''
Ejercicio 2.3.1
    Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''

def mostrarAños(edad):
    for i in range(1, edad+1):
        print(i)



def main():
    ok = False
    while not ok:
        try:
            edad = int(input("Introduce edad: "))

            if edad <= 0:
                print("La edad debe ser un número positivo.")
            else:
                mostrarAños(edad)
                ok = True
        except ValueError:
            print("Debes introducir un numero")
    

if __name__ == "__main__":
    main()