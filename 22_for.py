# Loop For
# Recorriendo estructuras
my_list = [23 , 45, 67, 89, 43, 57, 86, 12, 109]
for element in my_list:
  print(element)
my_tuple = ('nico','juli','santi')
print('-' * 20)
for element in my_tuple:
  print(element)
print('-' * 20)
my_dic = {
  'name': 'Camisa',
  'price': 100,
  'stock': 85
}
for key in my_dic:
  print(key,'=>',my_dic[key])
print('-' * 20)
for key, value in my_dic.items():
  print(key,'=>',value)
print('-' * 20)
# Listas de diccionarios
people = [
  {
    'name':'Nico',
    'age': 34
  },
  {
    'name':'Zule',
    'age': 45
  }
]
for person in people:
  print(person)
  print('Name =>',person['name'])
