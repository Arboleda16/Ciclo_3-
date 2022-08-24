# importamos las librerias

from tkinter import *
from tkinter import filedialog # para abrir el archivo
from pygame import mixer # para reproducir el archivo

# programamos metodos y botones

class musica:
    def init (self,ventana):
        ventana.geometry("400x400")
        ventana.title("Reproductor")
        ventana.config(bg="black",relief="ridge",bd="25")
         
        abr=Button(ventana,text="ABRIR",width=10,bg="red",relief="groove",bd="4")
        abr.place(x=50,y=50)
        repro=Button(ventana,text="REPRODUCIR",width=10,bg="red",relief="groove",bd="4")
        repro.place(x=50,y=100)
        paus=Button(ventana,text="PAUSAR",width=10,bg="red",relief="groove",bd="4")
        paus.place(x=50,y=150)
        det=Button(ventana,text="DETENER",width=10,bg="red",relief="groove",bd="4")
        det.place(x=50,y=200)
        self.abri_musica=False
        self.repro_musica=False
        
        
        ventana=Tk()
        imagen=PhotoImage(file="icono.png")
        Label(ventana,image=imagen).place(x=50,y=50)
        musica(ventana)
        ventana.mainloop()