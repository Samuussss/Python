"""
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

palabra[índice]
palabara[índice_negativo]
From left to right start of 0
From right to left start of -1
'ABC'[-1]
palabra[inicio:fin]
palabra[inicio:fin:pasos]
"""

# Solución 1
palabra_ingresada = input("ingrese una palabra: ")
cantidad_de_letras = len(palabra_ingresada)
comodin = -1
for i in range(cantidad_de_letras):
    print(palabra_ingresada[comodin])
    comodin -= 1


# Solución 2
palabra_ingresada = input("ingrese una palabra: ")
for i in palabra_ingresada[::-1]:
    print(i)