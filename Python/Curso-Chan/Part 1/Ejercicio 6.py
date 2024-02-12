"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
"""

# Esto muestra trinágulos alineados a la izquierda
# Solución 1
numero_entero = int(input("introduzca un numero continuacion: "))
triangulo_rectangulo = ["*"]
for i in range(numero_entero):
    print(''.join(triangulo_rectangulo))
    triangulo_rectangulo.append("*")


# Solución 2
numero_entero = int(input("introduzca un numero continuacion: "))
for i in range(numero_entero):
    print('*'*i)
