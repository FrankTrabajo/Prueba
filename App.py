import tkinter as tk
from tkinter import *
import math as m

class Ventana:

    def __init__(self, root):
        self.ventana = root
        self.ventana.title("Calculadora")
        self.ventana.resizable(1,1)
        self.ventana.geometry("470x400+240+120")
        
        self.variableA = 0
        self.variableB = 0
        self.ejecutor =""
        
        #Creacion del contenedor del Frame principal
        frame = LabelFrame(self.ventana, bg="cyan")
        frame.grid(row=0,column=0,columnspan=4,padx=20, pady=20)
        #Label donde se verá el resultado por pantalla
        self.ventanaNumerica = Label(frame, text="Introduzca una operacion", fg="grey")
        self.ventanaNumerica.grid(row=1,column=1)
        #Botones de numeros
        self.boton_Uno = Button(frame, text="1", width=10, command=self.boton_pres_uno)
        self.boton_Uno.grid(row=4, column=0, pady=10, padx=10)

        self.boton_Dos = Button(frame, text="2", width=10, command=self.boton_pres_dos)
        self.boton_Dos.grid(row=4, column=1, pady=10, padx=10)

        self.boton_Tres = Button(frame, text="3", width=10, command=self.boton_pres_tres)
        self.boton_Tres.grid(row=4, column=2, pady=10, padx=10)

        self.boton_Cuatro = Button(frame, text="4", width=10, command=self.boton_pres_cuatro)
        self.boton_Cuatro.grid(row=3, column=0, pady=10, padx=10)

        self.boton_Cinco = Button(frame, text="5", width=10, command=self.boton_pres_cinco)
        self.boton_Cinco.grid(row=3, column=1, pady=10, padx=10)

        self.boton_Seis = Button(frame, text="6", width=10, command=self.boton_pres_seis)
        self.boton_Seis.grid(row=3, column=2, pady=10, padx=10)

        self.boton_Siete = Button(frame, text="7", width=10, command=self.boton_pres_siete)
        self.boton_Siete.grid(row=2, column=0, pady=10, padx=10)

        self.boton_Ocho = Button(frame, text="8", width=10, command=self.boton_pres_ocho)
        self.boton_Ocho.grid(row=2, column=1, pady=10, padx=10)

        self.boton_Nueve = Button(frame, text="9", width=10, command=self.boton_pres_nueve)
        self.boton_Nueve.grid(row=2, column=2, pady=10, padx=10)

        self.boton_Cero = Button(frame, text="0", width=10, command=self.boton_pres_cero)
        self.boton_Cero.grid(row=5, column=0, pady=10, padx=10)

        #Botones de operaciones

        self.boton_suma = Button(frame, text="+", width=10, command=self.boton_suma)
        self.boton_suma.grid(row=5, column=1, pady=10, padx=10)

        self.boton_resta = Button(frame, text="-", width=10, command=self.boton_resta)
        self.boton_resta.grid(row=5, column=2, pady=10, padx=10)

        self.boton_solucion = Button(frame, text="=", width=10, command=self.boton_solucion)
        self.boton_solucion.grid(row=5, column=3, pady=10, padx=10)

        self.boton_multiplicar = Button(frame, text="*", width=10, command=self.boton_multiplicar)
        self.boton_multiplicar.grid(row=4, column=3, pady=10, padx=10)

        self.boton_dividir = Button(frame, text="/", width=10, command=self.boton_dividir)
        self.boton_dividir.grid(row=3, column=3, pady=10, padx=10)

        self.boton_borrar = Button(frame, text="Ce", width=10, command=self.boton_borrar)
        self.boton_borrar.grid(row=2, column=3, pady=10, padx=10)


    def boton_pres_cero(self):
        self.ventanaNumerica.config(text=0)
        if(self.variableA == 0):
            self.variableA = 0
        elif(self.variableB == 0):
            self.variableB = 0
    def boton_pres_nueve(self):
        self.ventanaNumerica.config(text=9)
        if(self.variableA == 0):
            self.variableA = 9
        elif(self.variableB == 0):
            self.variableB = 9
    def boton_pres_ocho(self):
        self.ventanaNumerica.config(text=8)
        if(self.variableA == 0):
            self.variableA = 8
        elif(self.variableB == 0):
            self.variableB = 8
    def boton_pres_siete(self):
        self.ventanaNumerica.config(text=7)
        if(self.variableA == 0):
            self.variableA = 7
        elif(self.variableB == 0):
            self.variableB = 7
    def boton_pres_seis(self):
        self.ventanaNumerica.config(text=6)
        if(self.variableA == 0):
            self.variableA = 6
        elif(self.variableB == 0):
            self.variableB = 6
    def boton_pres_cinco(self):
        self.ventanaNumerica.config(text=5)
        if(self.variableA == 0):
            self.variableA = 5
        elif(self.variableB == 0):
            self.variableB = 5
    def boton_pres_cuatro(self):
        self.ventanaNumerica.config(text=4)
        if(self.variableA == 0):
            self.variableA = 4
        elif(self.variableB == 0):
            self.variableB = 4
    def boton_pres_tres(self):
        self.ventanaNumerica.config(text=3)
        if(self.variableA == 0):
            self.variableA = 3
        elif(self.variableB == 0):
            self.variableB = 3
    def boton_pres_dos(self):
        self.ventanaNumerica.config(text=2)
        if(self.variableA == 0):
            self.variableA = 2
        elif(self.variableB == 0):
            self.variableB = 2
    def boton_pres_uno(self):
        self.ventanaNumerica.config(text=1)
        if(self.variableA == 0):
            self.variableA = 1
        elif(self.variableB == 0):
            self.variableB = 1

    def boton_suma(self):
        self.ejecutor = "+"
    def boton_resta(self):
        self.ejecutor = "-"
    def boton_multiplicar(self):
        self.ejecutor = "*"
    def boton_dividir(self):
        self.ejecutor = "/"
    def boton_borrar(self):
        self.ventanaNumerica.config(text="Introduce un numero")
        self.variableA = 0
        self.variableB = 0

    def boton_solucion(self):
        if(self.ejecutor == "+"):
            total = self.variableA + self.variableB
            self.ventanaNumerica.config(text=total)
            
        elif(self.ejecutor == "-"):
            total = self.variableA - self.variableB
            self.ventanaNumerica.config(text=total)
        elif(self.ejecutor == "*"):
            total = self.variableA * self.variableB
            self.ventanaNumerica.config(text=total)
        elif(self.ejecutor == "/"):
            total = self.variableA / self.variableB
            self.ventanaNumerica.config(text=total)
            

        self.variableA = 0
        self.variableB = 0



if __name__ == '__main__':
    root = Tk()
    app = Ventana(root)
    root.mainloop()