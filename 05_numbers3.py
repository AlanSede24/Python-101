# Solucion alternativa usando librería "mean" de statistics
# importa el modulo de statistics de python , el cual  permite realizar operaciones como suma,promedio,media etc. 
from statistics import mean
# capturar los valores correspondiente a cada mes
budgetEnero = int(input('Ingrese presupuesto de enero: '))
budgetFebrero = int(input('Ingrese presupuesto de febrero: '))
budgetMarzo = int(input('Ingrese presupuesto de marzo: '))
# hallar el promedio, dentro de '[]' se puede agregar los valores de los meses separados por comas
mean = mean([budgetEnero, budgetFebrero, budgetMarzo])
# imprime el promedio
print(f'El promedio de los meses es -> {round(mean,2)}')
