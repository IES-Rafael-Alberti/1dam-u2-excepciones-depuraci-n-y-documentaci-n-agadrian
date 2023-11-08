##### DEPURAR PROGRAMA #####
"""
#!usr/bin/env python3

Crea una función “CalcularMaxMin” que recibe una lista con valores numéricos y
devuelve el valor máximo y el mínimo. Crea un programa que complete una lista de numeros
aleatorios (entre 1 y 100) y muestre el máximo y el mínimo, utilizando la función anterior.
Por último, pide un número (entre 1 y 100) y el programa debe decir si está en la lista anterior.
"""

import random

def CalcularMaxMin(lista):
    return (max(lista),min(lista))


numeros = []

#Inicializo la lista con valores aleatorios
for i in range(0,5):
    numeros.append(random.randint(1,100))

vmax,vmin = CalcularMaxMin (numeros)
print("El valor máximo es ",vmax)
print("El valor mínimo es ",vmin)

numero = int(input("Dime un número del 1 al 100: "))
while numero < 1 or numero > 100:
    print("El número debe estar entre 1 y 100: ")
    numero = int(input())

if numero in numeros:
    print("El número está en la lista")
else:
    print("El número no está en la lista")  