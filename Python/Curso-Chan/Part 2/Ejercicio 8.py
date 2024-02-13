"""Hacer un programa que solicite una lista de números que corta cuando se
ingresa un cero y luego mostrar por pantalla el menor y el segundo menor."""

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
        print("cero detectado: ")
        print("------")
        break

if lista_de_numeros:
    lista_de_numeros.sort()
    menor_numero = lista_de_numeros[0]
    segundo_menor_numero = lista_de_numeros[1] if len(lista_de_numeros) > 1 else None
    print(f"El menor número ingresado es {menor_numero}.")
    if segundo_menor_numero is not None:
        print(f"El segundo menor número ingresado es {segundo_menor_numero}.")
    else:
        print("No se ingresaron suficientes números para encontrar el segundo menor.")
else:
    print("No se ingresaron números.")
print("-------------")
