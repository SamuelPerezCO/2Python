#Alcance de variables (scope)

var_global = 'Variable global'


def imprimir():
    #Acceder a una variable global
    global var_global
    print(f'Variable global desde una funcion: {var_global}')
    #Definicion de variable local
    var_local = 'Variable local'
    print(f'Variable local desde una funcion: {var_local}')
    var_global = 'Nuevo valor variable global'

    def funcion_anidada():
        print(f'Variable local dentro funcion anidada: {var_local}')

    funcion_anidada()

imprimir()
print(f'Variable global fuera funcion: {var_global}')
#No es posible acceder a variables locales fuera 
#del bloque que se definieron
#print(f'Var local fuerea funcion: {var_local}')