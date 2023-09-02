"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""
def interes():
    cantidad_a_invertir = int(input("introduzca la cantidad a invertir: $"))
    interes_anual = int(input("introduzca la cantidad a invertir: $"))    
    cantidad_de_años = int(input("introduzca la cantidad a invertir: $"))

    # cantidad_a_invertir * (1 + interes_anual) ** año
    for año in range(1, cantidad_de_años+1):
        resultado = cantidad_a_invertir * (1 + interes_anual) ** año
    
    return resultado


print(interes())