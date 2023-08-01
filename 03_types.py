import datetime
# Obtengo fecha actual para registro
current_date = datetime.datetime.now()
time_difference = datetime.timedelta(hours=-3)
date_format = current_date.strftime("%Y-%m-%d %H:%M:%S")
print(current_date + time_difference)
# String
name = 'Santiago'
print("Name:",name)
print("Data type:",type(name))
# int
age = 12
print("Age:",age)
print("Data type:",type(age))
# boolean
is_single = True
print("Is single:",is_single)
print("Data type:",type(is_single))
# inputs
nat = input("¿What's your nationality?")
print("Nationality:",nat)
print("Data type:",type(nat))

