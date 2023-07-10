"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""

def tabla_de_multiplicar():
    tabla_de_multiplicar = int(input("Ingrese la tabla del número a conocer: "))
    for i in range(1, 11):
        # i = 1 print(8*1)
        # i = 2 print(8*2)
        # ...
        # i = 10 print(8*10)
        print(tabla_de_multiplicar*i)

print(tabla_de_multiplicar())