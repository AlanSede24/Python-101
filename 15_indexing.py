# Indexing -> acceder a un elemento individual usando su índice (posición numérica)
text = "Sabe Python";print('Str.:\n' + text)
print('Búsqueda de elementos...')
print('Primera posición:',text[0])
print('Septima posición:',text[6])
last_pos = len(text) - 1 # Guarda la última posición
print('Última posición v1:',text[last_pos])
# Forma automática de buscar la última posición
print('Última posición v2:',text[-1])
print('-' * 20) # línea divisoria
# Slicing -> acceder a varios elementos especificando el rango de índices
print('Búsqueda por rangos...')
print('Rango 0 a 6:',text[0:6]) # vale tmb "text[:10]"
print('Rango 7 a 10:',text[7:10])
print('Rango 5 a final:',text[5:])
print('Rango completo:',text[:])
# Saltos (define el paso)
print('Rango 2 a 8, paso 1:',text[2:8:1])
print('Rango 2 a 8, paso 2:',text[2:8:2])
print('Rango completo, paso 3:',text[::3])
print('Rango completo, al revés:',text[::-1])




