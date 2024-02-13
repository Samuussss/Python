"""Hacer un programa que solicite la edad de un grupo de personas. El programa
deberá pedir edades hasta que se ingrese una edad menor a 18 años. Deberá
mostrar por pantalla cuántas personas mayores se registraron."""

viejos = 0

while True:
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        viejos += 1
    else:
        break

print(f"Personas mayores de 18 años registradas: {viejos}")
