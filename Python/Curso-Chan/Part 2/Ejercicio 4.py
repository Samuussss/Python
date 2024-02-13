"""Hacer un programa que solicite dos números y luego muestre los números
entre el menor y el mayor de ellos. Acordate, usando While."""

print("----------")
numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))
print("----------")

Cantidad_de_numeros_mostrados = 0

while True:
    
    if numero2 > numero1:
        numero1 += 1
        Cantidad_de_numeros_mostrados += 1
        print(numero1)
        numero_alterno1 = numero2 - 1
        if numero1 == numero_alterno1:
            break

    elif numero2 < numero1:
        numero1 -= 1
        Cantidad_de_numeros_mostrados += 1
        print(numero1)
        numero_alterno2 = numero2 + 1
        if numero1 == numero_alterno2:
            break

    elif numero2 == numero1:
        print("los numeros son iguales, Reintentelo.")
        break
if Cantidad_de_numeros_mostrados >= 1:
    print("------")
    print(f"La Cantidad de numeros mostrados es: {Cantidad_de_numeros_mostrados}")
print("----------")
