# Error al comparar floats (precisión decimal)
x = 3.3
y = 1.1 + 2.2
print("x ->",x),print("y ->",y)
print("Comparación1:", x == y)
print("-" * 20) # linea divisoria
# Solución convirtiendo a strings
y_str = format(y,".2g")
print("y_str ->", y_str)
print("Comparación2:", str(x) == y_str)
print("-" * 20) # linea divisoria
# Solución numérica
# se establece un umbral de tolerancia
tolerance = 0.00001
print("Comparación3:", abs(x - y) < tolerance)
if (abs(x - y) < tolerance):
  print("¡Cumple tolerancia!")
  # implemencación bucle if
  