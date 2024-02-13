"""Hacer un programa que solicite una lista de números que corta cuando se
ingresa un cero y luego mostrar por pantalla el máximo de ellos y la posición
en la que fue ingresado."""

print("-------------")
lista_de_numeros = []

mostrar_segundo_numero = False

if mostrar_segundo_numero == False:
    siguiente_numero = "primer"
elif mostrar_segundo_numero == True:
    siguiente_numero = "siguiente"

while True:
    numeros_ingresado = int(input(f"ingrese el {siguiente_numero} numero: "))
    mostrar_segundo_numero = True
    if numeros_ingresado > 0:
        lista_de_numeros.append(numeros_ingresado)
    elif numeros_ingresado == 0:
        print("------")
        print("cero detectado.")
        print("------")
        break

"""máximo de los números ingresados y su posición"""

if lista_de_numeros:
    maximo_numero = max(lista_de_numeros)
    posicion_maximo = lista_de_numeros.index(maximo_numero)
    print(f"El máximo número ingresado es {maximo_numero} y se encuentra en la posición {posicion_maximo}.")
else:
    print("No se ingresaron números.")
print("-------------")
