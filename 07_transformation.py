# Transformación dinámica
name = "Nicolas"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))
# Qué se puede y qué no
print("Nicolas" + " Molina")  #se puede
print(10 + 20)          # se puede
# print("Nicolas" + 12)   # dará error por mezclar str con int

# Concatenación y suma que andan
age = 12
print("v1:","Su edad es " + str(age))
print("v2:",f"Su edad es {age}")
age = input("Escribe tu edad -> ")
print(type(age))
print(f"Tu edad en 10 años será {int(age)+10}")
