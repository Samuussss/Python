"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase. 
"""

frase = input('ingrese una frase: ') # Hola como estas
letra = input('ingrese una letra: ') # a
contador = 0  # 2 

# i = 'H'
# i = 'o'
# i = 'l'
# i = 'a'
# i = ' '
for i in frase:
    if i == letra:
        contador += 1
    
print(f'Contador: {contador}')
