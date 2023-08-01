# Vamos un poco más allá con los strings
# Consulta si un string está dentro de otro con "in"
text1 = 'Sabe programar en Python'
print('Texto 1:\n' + text1)
text2 = 'Python'
print('Texto 2:\n' + text2)
print('Comparación:')
if (text2 in text1):
  print('Hay coincidencia')
else:
  print('No hay coincidencia')
# Longitud de los strings
size1 = len(text1); size2 = len(text2)
print("Tamaño 1:", size1)
print("Tamaño 2:", size2)
text1 = text1.upper() # Pasa todo a mayúsculas
print('Texto1 en Mayus.:\n' + text1)
text1 = text1.lower() # Pasa todo a minúsculas
print('Texto1 en Minus.:\n' + text1)
letter = text1.count('a') # Cuenta el número de apariciones de la letra 'a'
print('N° de veces que aparece la "a":\n' + str(letter)) # pasa a str para poder concatenar
text3 = 'Perro Blanco'
text3 = text3.swapcase() # intercambia may. por min. y viceversa
print('Texto swapeado:\n' + text3)
print(text3.startswith("pERRO")) # consulta si el string comienza con "Perro"
print(text3.endswith("bLANCO")) # consulta si el string comienza con "Perro"
print(text3.replace('bLANCO', 'nEGRO')) # hace el reemplazo de strings
text4 = 'gato bonito'
print('capitalize:',text4.capitalize()) # pone en may. la primera letra del str
print('title:',text4.title()) # pone en may. las primeras letras de las palabras
print("389".isdigit()) # identifica si es o no un posible número

