# Diccionarios
print('Diccionario:')
person = {
  'name': 'Nico',
  'last_name': 'Molina',
  'age': 25,
  'pr_langs': ['Python','JavaScript']
}
print(person);print('-' * 20)
# Actualizar atributos del dic
print('Dic. actualizado:')
person['name'] = 'Santi'
person['age'] -= 3
person['pr_langs'].append('Rust')
print(person);print('-' * 20)
# Eliminar atributos del dic
print('Borrando atributos del dic.:')
del person['last_name']
person.pop('age')
print(person);print('-' * 20)
# Métodos útiles
print('Items:');print(person.items())
print(person);print('-' * 20)
print('Keys:');print(person.keys())
print(person);print('-' * 20)
print('Values:');print(person.values())
print(person);print('-' * 20)