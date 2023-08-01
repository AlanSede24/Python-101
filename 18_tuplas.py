# Tuplas
print('Tupla numbers:')
numbers = (1, 3, 4, 8)
print(numbers,type(numbers))
print('-' * 20);print('Tupla strings:')
strings = ('Hola','feliz', 'mundo')
print(strings,type(strings))
print('Posición donde aparece "feliz":',strings.index('feliz'))
print('-' * 20);print('Tupla mix:')
mix = (True, 10, 'potter')
print(mix,type(mix))
print('Tercer elemento:',mix[2])
print('Veces que aparece "True":',mix.count(True))
print('-' * 20)
# Convertir de tupla a lista
print('Convertir tupla strings a lista:')
my_list = list(strings)
my_list[1] = 'maravilloso'
print(my_list,type(my_list))
print('Se actualiza pos.1');print('-' * 20)
# Convertir de lista a tupla
print('Convertir de lista a tuple:')
my_tuple = tuple(my_list)
print(my_tuple,type(my_tuple));print('-' * 20)
