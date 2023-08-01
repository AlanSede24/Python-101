# CRUD: Create, Read, Update & Delete
# Métodos útiles para listas
print('Lista inicial:')
numbers = [1, 2, 3, 4, 5]
print(numbers);print('-' * 20)
print('Agrega un elemento al final:')
numbers.append(30)
print(numbers);print('-' * 20)
print('Inserta un string en la pos. 0:')
numbers.insert(0,'hola')
print(numbers);print('-' * 20)
print('Inserta un string en la pos. 3:')
numbers.insert(3,'mundo') # inserta y desplaza los sig. a la derecha
print(numbers);print('-' * 20)
print('Cambia el elemento "3":')
index = numbers.index(3) # guarda la posición del elemento "3"
numbers[index] = 'changed'
print(numbers);print('-' * 20)
print('Quita el elemento "5":')
numbers.remove(5) # quita el elemento "5"
print(numbers);print('-' * 20)
print('Quita el último elemento:')
numbers.pop() # quita el último elemento de la lista
print(numbers);print('-' * 20)
print('Quita el primer elemento:')
numbers.pop(0) # quita el primer elemento de la lista
print(numbers);print('-' * 20)
print('Pone la lista al revés:')
numbers.reverse() # hace que la lista esté al revés
print(numbers);print('-' * 20)
print('Ordena de menor a mayor:')
numbers_a = [3, 7, 5, 2]
numbers_a.sort() # ordena de menor a mayor los n° de la lista
print(numbers_a);print('-' * 20)
print('Ordena alfabéticamente:')
string = ['c','x','e','a','r','f']
string.sort() # ordena la lista de strings en orden alfabético
print(string);print('-' * 20)
