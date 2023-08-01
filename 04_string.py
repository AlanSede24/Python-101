# Variables
first_name = "Nicolas"
last_name = "Molina Monroy"
# Intercambiar comillas simples y dobles para solucionar errores
quote1 = "He's Nicolas."
quote2 = 'He said "Hello..."'
# Concatenación de 3 strings
full_name = first_name + " " + last_name
# Muestra por consola
#print(first_name,last_name)
print(full_name)
print(quote1,quote2)
# format
template1 = "Hola, mi nombre es " + first_name + " y mi apellido es " + last_name
template2 = "Hola, mi nombre es {} y mi apellido es {}".format(first_name,last_name)
template3 = f"Hola, mi nombre es {first_name} y mi apllido es {last_name}"
print("v1:",template1)
print("v2:",template2)
print("v3:",template3)
