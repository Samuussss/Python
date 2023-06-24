"""Hacer una calculadora sencilla que multiplique sume, reste, multiplique y divida por 2, dando al operador a elejir una de las ya mencionadas"""
def calculadora():
    operacion = input("¿Qué operación deseas realizar? (+, -, *, /, /2): ")
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    elif operacion == "*":
        resultado = num1 * num2
    elif operacion == "/":
        resultado = num1 / num2
    elif operacion == "/2":
        resultado = num1 / 2
    else:
        print("Operación no válida.")
        return

    print(f"El resultado es: {resultado}")
    print("Hasta luego!")

calculadora()
