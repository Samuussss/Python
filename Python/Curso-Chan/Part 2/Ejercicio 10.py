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
numeros_positivos.sort()
menor_numero_positivo = numeros_positivos
print(f"el menor número positivo es: {menor_numero_positivo}.")

Numeros_negativos.max()
mayor_numero_negativo = numeros_negativos
print(f"el mayor número negativo es {mayor_numero_negativo}.")