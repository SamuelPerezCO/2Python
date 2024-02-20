#Profundizando en set
#Un set es una coleccion de elementos unicos y es mutable
#los elementos de un set deben ser inmutablese
#conjunto = {}
conjunto = {'Juan' , True , 18.0}
print(conjunto)
#Set vacio
#conjunto = {}
#print(type(conjunto))
conjunto = set()
print(conjunto)
print(type(conjunto))
#Mutable 
conjunto.add('Juan')
print(conjunto)
#Contiene valores unicos
conjunto.add('Juan')
print(conjunto)
#crear un set apartir de un iterable
conjunto = set([4,5,7,8,4])
print(conjunto)
#Podemos agregar mas elementos o incluso otro set
conjunto2 = {100 , 200 , 300, 300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20,30,40,40])
print(conjunto)

#Copiar un set(copia poco profunda , solo copia referencias)
conjunto_copia = conjunto.copy()
print(conjunto_copia)

#Verifica la igualdad
print(f'Es igual en contenido?: {conjunto == conjunto_copia}')
print(f'Es la misma referencia? {conjunto is conjunto_copia}')

#Operaciones de conjunto con set 
#Personas con distintas caracteristicas
print('Otro video'.center(50 , '-'))
pelo_negro = {'Juan' , 'Karla' , 'Pedro' , 'Maria'}
pelo_rubio = {'Lorenzo' , 'Laura' , 'Marco'}
ojos_cafe = {'Karla' , 'Laura'}
menores_30 = {'Juan' , 'Karla' , 'Maria'}
#Todos con ojos_cafe y pelo rubio (union) no se repiten los elementos
print(ojos_cafe.union(pelo_rubio))
#Invertir el orden con el mismo resultado ( conmutativa)
print(pelo_rubio.union(ojos_cafe))

#(intersection) Solo las personas con ojos cafe y pelo rubio (conmutativa)
print(ojos_cafe.intersection(pelo_rubio))

#(difference) pelo negro sin ojos cafe (No es conmutativa)
#Las personas que se encuentran en el primer set pero no en el segundo
print(pelo_negro.difference(ojos_cafe))

#(diferencia simetrica) Pelo negro u ojos cafe , pero no ambos (conmutativa)
print(pelo_negro.symmetric_difference(ojos_cafe))

#Preguntar si un set esta contenido en otro(subset)
#revisamos si los elementos del primer set estan cotenidos en el segundo set
print(menores_30.issubset(pelo_negro))

#Preguntar si un set contiene a otro set(superset)
#Revisar si los elementos del primer set estan contenidos en el segundo set
print(menores_30.issuperset(pelo_negro))

#Preguntar si los de pelo negro no tienen pelo rubio (distjoint)
print(pelo_negro.isdisjoint(pelo_rubio))