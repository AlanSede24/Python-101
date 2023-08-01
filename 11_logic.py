# Operadores lógicos AND y OR
print("T and T ->", True and True)
print("T and F ->", True and False)
print("F and T ->", False and True)
print("F and F ->", False and False)
print("-" * 20) # linea divisoria
print("T or T ->", True or True)
print("T or F ->", True or False)
print("F or T ->", False or True)
print("F or F ->", False or False)
print("-" * 20) # linea divisoria
print(10 > 5 and 7 > 2)
print(10 < 2 or 6 < 10)

# Ejemplo práctico AND
stock = int(input("Ingrese el n° de stock -> ")) # como es string, lo pasa a int
if (stock >= 100 and stock <= 1000): # regla de negocio
  print("¡Se cumple! Stock correcto")
else:
  print("No se cumple :(, stock incorrecto")

# Ejemplo práctico OR
role = input("Ingrese el rol ->")
if(role == "admin" or role == "seller"):
  print("Puede ingresar :D")
else:
  print("Rol desconocido")
  