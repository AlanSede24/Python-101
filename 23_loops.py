# Loops anidados
matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]
         ]
print(matriz)
print('Elemento 2|2:', matriz[1][1])
print('Elemento 1|3:', matriz[0][2])
for row in matriz:
  print('Fila -> ', row)
  for column in row:
    print(column)

