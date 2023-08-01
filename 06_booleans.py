# Los tipos de datos boolean solo tienen dos estados posibles: True y False
is_single = True
print("v1:",is_single)
print("v2:",not is_single) # invierte el estado
print(type(is_single))

# Interpretaciones como boolean
print(bool(True),bool(False),bool(None))
print(bool(0),bool(-1),bool("casa"))
print(bool(24),bool(0.0),bool(0.j))
print(bool(1),bool([]),bool(""))