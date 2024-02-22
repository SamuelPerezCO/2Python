import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('C:\\Programacion\\Proyectos\\2Python\\Seccion 57\\icono.ico')

#Metodos de los eventos 
def evento1():
    boton1.config(text='Boton 1 presionado')

def evento2():
    boton2.config(text='Boton 2 Presionado')

#Definimos dos botones 
boton1 = ttk.Button(ventana , text='Boton 1' , command=evento1)
boton1.grid(row=0, column=0 , sticky="w")

# N(Arriba) , E(Derecha) , S(Abajo) , W(Izaquierda)
boton2 = ttk.Button(ventana , text='Boton2' , command=evento2)
boton2.grid(row=1, column=0 , sticky='E')

ventana.mainloop()