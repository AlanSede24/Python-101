# Proyecto Piedra, Papel o Tijera
import random
import time
# Reglamento
print("REGLAS DEL JUEGO");print('-' * 30)
print("Opciones posibles: pi | pa | ti");print('-' * 30)
# Lógica del juego
round = 1
while (1):
  print('** ROUND N°', round,'**')
  round += 1
  user_option = input('Elija su opción ->')
  user_option = user_option.lower()    # pasa a minúsculas el string ingresado 
  tupla = ("pi", "pa", "ti")
  if user_option in tupla:
    random.seed(time.time())    # establece una semilla distinta en cada ejecución (util para el algoritmo de generación de numeros aleatorios).
    numero_random = random.randint(1,3) # genera n° entero random entre 1 y 3
    #print("N° random ->", numero_random)
    computer_option = tupla[numero_random - 1]
    print("Opción del usuario ->",user_option)
    print("Opción de la máquina ->",computer_option)
    print('-' * 30)
    if user_option == computer_option:
      print('¡Empate!')
    elif (user_option == "pi" and computer_option == "ti") or (user_option == "pa" and computer_option == "pi") or (user_option == "ti" and computer_option == "pa"):
      print('¡Gana el usuario! Felicidades :D')
    else:
      print("¡Pierde el usuario! Ánimo, puedes intentarlo de nuevo.")
  else:
    print("La opción ingresada NO es válida. ¡Prueba otra vez!")
  print('-' * 30)
# Alternativa para elegir una opción de forma aleatoria
# computer_option = random.choice(tupla)
