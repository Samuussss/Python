"""Hacer un programa que solicite una lista de números que corta cuando se
ingresa un cero y luego emitir por pantalla el máximo de los números
negativos y el mínimo de los números positivos."""
print("--------------------")
numeros_negativos = []
numeros_positivos = []

while True:
    numero_ingresado = int(input("ingrese un numero: "))
    
    if numero_ingresado == 0:
        print("------")
        print("cero detectado")
        print("------")
        break

    elif numero_ingresado < 0:
        numeros_negativos.append(numero_ingresado)
    elif numero_ingresado > 0:
        numeros_positivos.append(numero_ingresado)

print(f"el menor número positivo es: {sorted(numeros_positivos)[0]}.")
print(f"el mayor número negativo es {max(numeros_negativos)}.")
print("--------------------")