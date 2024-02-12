"""
Ejercicio 3: Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

numero_entero = int(input("Introduzca un numero entero positivo a continuacion: "))

"""
Número entero ingresado: 10
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Variable i: 0
Variable i: 1
Variable i: 2
"""
for i in range(numero_entero):
    if i % 2 != 0:
        print(i, end=", ")