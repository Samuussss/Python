"""Hacer un programa para ingresar una lista de números que corta cuando se
ingresa un cero y luego mostrar: la cantidad de números primos, la cantidad de
números pares, la cantidad de positivos y la cantidad de negativos"""

#! !!!DANGER ZONE!!!

#? Cuidadito de no confundirse Cabron 
#? QUE TE METO UNA HOSTIA JODER QUE CULPA DE ESO HICISTE UNA FUNCION 
#? TOTALMENTE MAL CABRON

numero_ingresados_lista = []

numeros_primos = []
numeros_pares = []
numeros_positivos = []
numeros_negativos = []

#! !!!DANGER ZONE!!!

# Bucle Infinito que pide números hasta que se ingresa un "0"
while True:
    numero_ingresado = int(input("ingrese un numero: "))
    numero_ingresados_lista.append(numero_ingresado)

# Si el Numero es 0 Se finaliza el bucle
    if numero_ingresado == 0:
        print("------")
        print("cero detectado")
        print("------")
        break

# Si es Primo se le añade a la lista
    elif numero_ingresado // 2 == 0:
        numeros_primos.append(numero_ingresado)

# Si es Par se le añade a la lista
    elif numero_ingresado % 10 == (0, 2, 4, 6, 8):
        numeros_pares.append(numero_ingresado)

# Si es Positivo se le añade a la lista
    elif numero_ingresado >= 1:
        numeros_positivos.append(numero_ingresado)

# Si es Negativo se le añade a la lista
    elif numero_ingresado <= -1:
        numeros_negativos.append(numero_ingresado)


# Imprimimos las listas en el caso que no esten vacias
if numeros_primos >= 1:
    print(f"los numeros primos son: {numeros_primos}")

if numeros_pares >= 1:
    print(f"los numeros pares son: {numeros_pares}")

if numeros_positivos >= 1:
    print(f"los numeros Positivos son: {numeros_positivos}")

if numeros_negativos <= -1:
    print(f"los numeros Negativos son: {numeros_negativos}")
