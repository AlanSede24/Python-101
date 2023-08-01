# Diccionarios
print('Diccionario:')
my_dict = {
  'name': 'Nicolas',
  'last_name': 'Molina Monroy',
  'age': 35
} # definición del diccionario (forma clave - valor)
print(my_dict);print(type(my_dict))
# Consultas
print('Longitud:',len(my_dict))
print('Busca "age" v1:', my_dict['age'])
print('Busca "age" v2:', my_dict.get('age')) # alternativa útil cuando se busca algo que pueda no estar en el dic
print('Busca "last_name":', my_dict['last_name'])
print('¿Está "name" en el dic.?','name' in my_dict)
