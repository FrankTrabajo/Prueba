import tkinter as tk
from tkinter import *

class Ventana:

    def __init__(self, root):
        self.ventana = root
        self.ventana.title("Calculadora")
        self.ventana.resizable(1,1)
        self.ventana.geometry("400x600+240+120")
        
        variableA=0
        variableB=0
        ejecutor=""
        
        #Creacion del contenedor del Frame principal
        frame = LabelFrame(self.ventana, bg="cyan")
        frame.grid(row=0,column=0,columnspan=4,padx=20, pady=20)
        #Label donde se verá el resultado por pantalla
        self.ventanaNumerica = Label(frame, text="Introduzca una operacion", fg="grey")
        self.ventanaNumerica.grid(row=1,column=1)
        #Botones de numeros
        self.boton_Uno = Button(frame, text="1", width=10, command=self.boton_pres)
        self.boton_Uno.grid(row=4, column=0, pady=10, padx=10)

        self.boton_Dos = Button(frame, text="2", width=10, command=self.boton_pres)
        self.boton_Dos.grid(row=4, column=1, pady=10, padx=10)

        self.boton_Tres = Button(frame, text="3", width=10, command=self.boton_pres)
        self.boton_Tres.grid(row=4, column=2, pady=10, padx=10)

        self.boton_Cuatro = Button(frame, text="4", width=10, command=self.boton_pres)
        self.boton_Cuatro.grid(row=3, column=0, pady=10, padx=10)

        self.boton_Cinco = Button(frame, text="5", width=10, command=self.boton_pres)
        self.boton_Cinco.grid(row=3, column=1, pady=10, padx=10)

        self.boton_Seis = Button(frame, text="6", width=10, command=self.boton_pres)
        self.boton_Seis.grid(row=3, column=2, pady=10, padx=10)

        self.boton_Siete = Button(frame, text="7", width=10, command=self.boton_pres)
        self.boton_Siete.grid(row=2, column=0, pady=10, padx=10)

        self.boton_Ocho = Button(frame, text="8", width=10, command=self.boton_pres)
        self.boton_Ocho.grid(row=2, column=1, pady=10, padx=10)

        self.boton_Nueve = Button(frame, text="9", width=10, command=self.boton_pres)
        self.boton_Nueve.grid(row=2, column=2, pady=10, padx=10)

        self.boton_Cero = Button(frame, text="0", width=10, command=self.boton_pres)
        self.boton_Cero.grid(row=5, column=0, columnspan=2, pady=10, padx=10)


    def boton_pres(self):

        if(self.boton_Cero):
            self.ventanaNumerica.config(text=0)
        if(self.boton_Nueve):
            self.ventanaNumerica.config(text=9)
        if(self.boton_Ocho):
            self.ventanaNumerica.config(text=8)
        if(self.boton_Siete):
            self.ventanaNumerica.config(text=7)
        if(self.boton_Seis):
            self.ventanaNumerica.config(text=6)
        if(self.boton_Cinco):
            self.ventanaNumerica.config(text=5)
        if(self.boton_Cuatro):
            self.ventanaNumerica.config(text=4)
        if(self.boton_Tres):
            self.ventanaNumerica.config(text=3)
        if(self.boton_Dos):
            self.ventanaNumerica.config(text=2)
        if(self.boton_Uno):
            self.ventanaNumerica.config(text=1)

    



if __name__ == '__main__':
    root = Tk()
    app = Ventana(root)
    root.mainloop()