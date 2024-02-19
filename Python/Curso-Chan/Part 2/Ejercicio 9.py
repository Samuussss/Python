"""Realizar el nuevamente el ejercicio 8 pero ahora debe devolver además la
posición en la que fue encontrado cada uno de los mínimos."""

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



else:
    print("No se ingresaron números.")
print("-------------")