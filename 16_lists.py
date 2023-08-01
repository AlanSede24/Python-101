# Listas
print('Listas...')
numbers = [1, 2, 3, 4]
tasks = ['Do the dishes', 'Play videogames']
types = [10, True, 'Hola']
print(numbers,type(numbers));print(tasks);print(types)
print('Primeros elementos de las listas:')
print(numbers[0]);print(tasks[0]);print(types[0])
text = 'Hola Mundo'
# text[0] = 'W' -> ¡no se puede!
print('-' * 20)
# Actualizar primer posición de la lista
tasks[0] = 'Watch Platzi courses'
print("Actualiza primer elemento:");print(tasks)
# Seleccionar subconjunto (slicing)
print(numbers[:3])
# Busca un elemento dentro de una lista
print('Resultado búsqueda:',10 in types)

