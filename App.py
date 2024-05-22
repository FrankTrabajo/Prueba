import tkinter as tk
from tkinter import *

class Ventana:

    def __init__(self, root):
        self.ventana = root
        self.ventana.title("Calculadora")
        self.ventana.resizable(1,1)
        
        #Creacion del contenedor del Frame principal
        frame = LabelFrame(self.ventana, text="Calculadora",font=('Calibri', 16, 'bold'))
        frame.grid(row=0,column=0,columnspan=4,padx=20, pady=20)
        #Label donde se verá el resultado por pantalla
        self.ventanaNumerica = Label(frame)
        self.ventanaNumerica.grid(row=0,column=0, sticky=N + E)
        #Botones de numeros



if __name__ == '__main__':
    root = Tk()
    app = Ventana(root)
    root.mainloop()