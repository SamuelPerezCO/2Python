import math
from decimal import Decimal

#NaN - Not a number (No es un Numero)
#NaN no es sensible a mayusculas/minusculas
#NaN es un tipo de dato numero indefinido
a = float('NaN')
#print(f'a: {a}')
#print(f'Es NaN (Not a number?): {math.isnan(a)}')

a = Decimal('NaN')
print(f'a: {a}')
print(f'Es NaN (Not a number?): {math.isnan(a)}')