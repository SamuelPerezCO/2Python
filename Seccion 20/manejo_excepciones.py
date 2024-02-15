from NumerosIdenticosException import *

resultado = None
try:
    a = int(input('Primer Numero : '))
    b = int(input('Segundo Numero: '))
    if a == b:
        raise NumerosIdenticosException('Numeros Identicos')
    resultado = a/b
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrio un error: {e} , {type(e)}')
except TypeError as e:
    print(f'TypeError - Ocurrio un error: {e}' , {type(e)})
except Exception as e:
    print(f'Exception - Ocurrio un error: {e}' , {type(e)})
else:
    print('No se arrojo ninguna excepcion')
finally:
    print('Ejecicion del bloque finally')

print(f'Resultado: {resultado}')
print('Continuamos..')