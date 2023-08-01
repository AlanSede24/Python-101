# Inputs
budget_january = float(input("Ingrese presupuesto correspondiente a Enero -> "))
budget_february = float(input("Ingrese presupuesto correspondiente a Febrero -> "))
budget_march = float(input("Ingrese presupuesto correspondiente a Marzo -> "))
# Sum and Average
# se trabaja sobre el array con las funciones sum y len, sumando todos los elementos y dividiendo por su longitud
budget = [budget_january, budget_february, budget_march]
avr = sum(budget)/len(budget)
# Print on display
print("El promedio trimestral es:",round(avr,2))
