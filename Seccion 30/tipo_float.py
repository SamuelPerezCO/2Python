#Profundizando tipo float
a = 3.0
#Constructor float puede recibir int y str
a = float(10)
a = float('10')
#Notacion exponencial (Valores positivos o negativos)
a = 3e5
a = 3e-5
#print(f'a: {a:.5f}')
#Cualquier calculo que involucre un float , se promueve un float
a = 4.0 + 5
print(a)
print(type(a))