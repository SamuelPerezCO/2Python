#Decoradores
#un decorador es una funcion que recibe una funcion y regresa otra
#La utilizamos para extender funcionalidad
#1. Funcion decorador(a)
#2. Funcion a decorar(b)
#3. Funcion decorada(c)

def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args , **kwargs):
        print('Antes de ejecutar la funcion')
        resultado = funcion_a_decorar_b(*args , **kwargs)
        print('Despues de ejecutar la funcion')
        return resultado
    return funcion_decorada_c

@funcion_decorador_a
def sumar(a , b):
    return a + b

resultado = sumar(5,6)
print(f'Resultado suma: {resultado}')