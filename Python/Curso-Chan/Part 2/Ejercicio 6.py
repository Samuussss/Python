"""Hacer un programa que solicite UN número y luego calcule y emita un cartel
aclaratorio si el mismo es primo o no es primo.
Nota: usando While. Ya lo hicimos con FOR, ahora con While."""

numero = int(input("Ingrese un número entero positivo mayor que 1: "))
es_primo = True

if numero > 1:
    divisor = 2
    while divisor <= numero / 2:
        if numero % divisor == 0:
            es_primo = False
            break
        divisor += 1
else:
    es_primo = False
if es_primo:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
