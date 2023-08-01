# Condicionales
print("perro | gato | tigre | cocodrilo")
print('-' * 30)
pet = input("¿Cuál es su mascota favorita según la lista anterior? ->")
if (pet == "perro" or pet == "gato"):
  print("¡Tu elección es muy amigable!")
elif(pet == "tigre" or pet == "cocodrilo"):
  print("¡Tu elección es muy peligrosa!")
else:
  print("Esa mascota no está en la lista.")

# ejercicio par o impar
number = int(input("Ingrese un número entero positivo ->"))
if((number % 2) == 1 and number > 0):
  print("El número ingresado es impar.")
elif (number > 0):
  print("El número ingresado es par.")
else:
  print("Ingresaste un n° inválido.")
  