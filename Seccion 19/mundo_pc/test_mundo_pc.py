from teclado import *
from raton import *
from monitor import *
from computador import *
from orden import *

teclado1 = Teclado('HP' , 'USB')
raton1 = Raton('HP' , 'USB')
monitor1 = Monitor('HP' , 15)
computadora1 = Computadora('HP' , monitor1 , teclado1 , raton1)

teclado2 = Teclado('Acer' , 'Blue')
raton2 = Raton('Acer' , 'Blue')
monitor2 = Monitor('Acer' , 27)
computadora2 = Computadora('Acer' , monitor2 , teclado2 , raton2)

teclado3 = Teclado('Gamer' , 'blue')
raton3 = Raton('Gamer' , 'blu')
monitor3 = Monitor('Gamer' , 34)
computadora3 = Computadora('Asus' , monitor3 , teclado3 , raton3)

computadora1 = [computadora1 , computadora2]
orden1 = Orden(computadora1)
#print(orden1)
orden1.agregar_computadora(computadora3)
print(orden1)

computadoras2 = [computadora2 , computadora3]
orden2 = Orden(computadoras2)
print(orden2)