# Loop While
counter = 0
while counter < 5:
  counter += 1
  print('Contador 1:', counter)
print('-' * 20)
# Detener el loop
counter = 0
while counter < 7:
  counter += 1
  if counter == 5:
    break # detiene de forma forzada
  print('Contador 2:', counter)
print('-' * 20)
# Saltar iteraciones
counter = 0
while counter < 8:
  counter += 1
  if counter < 3:
    continue # salta a la siguiente iteración (evitando lo de abajo)
  print('Contador 3:', counter)
  
  