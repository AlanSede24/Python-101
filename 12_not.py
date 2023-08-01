# Operador NOT
print("not T ->",not True)
print("not F ->",not False)
print("-" * 20) # linea divisoria
# Operador NAND (implementado con NOT y AND)
print("T nand T ->", not(True and True))
print("T nand F ->", not(True and False))
print("F nand T ->", not(False and True))
print("F nand F ->", not(False and False))
print("-" * 20) # linea divisoria
# Operador NOR (implementado con NOT y OR)
print("T nor T ->", not(True or True))
print("T nor F ->", not(True or False))
print("F nor T ->", not(False or True))
print("F nor F ->", not(False or False))
