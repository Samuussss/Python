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
    lista_ordenada = sorted((valor, indice) for indice, valor in enumerate(lista_de_numeros))
    menor_numero, pos_menor = lista_ordenada[0]
    segundo_menor_numero, pos_segundo_menor = lista_ordenada[1] if len(lista_ordenada) > 1 else (None, None)
    
    print(f"El menor número ingresado es {menor_numero} y se encuentra en la posición {pos_menor}.")
    
    if segundo_menor_numero is not None:
        print(f"El segundo menor número ingresado es {segundo_menor_numero} y se encuentra en la posición {pos_segundo_menor}.")
    else:
        print("No se ingresaron suficientes números para encontrar el segundo menor.")
else:
    print("No se ingresaron números.")
print("-------------")