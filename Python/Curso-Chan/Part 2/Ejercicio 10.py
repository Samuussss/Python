"""Hacer un programa que solicite una lista de números que corta cuando se
ingresa un cero y luego emitir por pantalla el máximo de los números
negativos y el mínimo de los números positivos."""

numeros_negativos = []
numeros_positivos = []

while True:
    numero_ingresado = int(input("ingrese un numero"))
    
    if numero_ingresado == 0:
        print("------")
        print("cero detectado")
        print("------")
        break

    elif numero_ingresado < 0:
        numeros_positivos.append(numero_ingresado)
    elif numero_ingresado > 0:
        numeros_positivos.append(numero_ingresado)