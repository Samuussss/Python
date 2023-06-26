"""
Ejercicio 2: Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

# Para que el usuario ingrese números => int(input("Ingrese el dato: "))
edad = int(input("Ingrese su edad: "))

# Edad es una palabra y no un número entero
# Reglamentación de código range(1, edad+1)
for i in range(1, edad+1):
    print(i)
