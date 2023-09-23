from tkinter import Tk
import interfaz
import datetime
import calendar
import observador
from observador import ruta

def decorador(cls):
    class Envoltura():

        def __init__(self, *args):
           self.instancia_de_clase=cls(*args) 
        
        def registrar_txt():
            archivo = open( ruta, "a") 
            archivo.write("ULTIMO INGRESO: " + (datetime.datetime.today().strftime("%H:%M:%S--%A %d/%m/%y")) + "\n")
            archivo.close()
        registrar_txt()

    return Envoltura

@decorador
class Control():

    def __init__(self, main):
        #print("# CONTROL.PY / CONSTRUCTOR / self ----------#",id(self))
        self.main_control=main # toma la ventana = main, y se la pasa a Ventanita()
        #print("1 CONTROL.PY / CONSTRUCTOR / main-------------------1",id(main))
        
        self.objeto_vista=interfaz.Ventanita(self.main_control) # y Ventanita ejecuta su constructor en el modulo interfaz.py
        #print("# CONTROL.PY / CONSTRUCTOR / self-----------#",id(self))
        #PATRON OBSERVADOR
        self.el_observador=observador.ConcreteObserverA(self.objeto_vista.objeto_base)

if __name__=="__main__":
    main=Tk()
    #print("0 CONTROL.PY / INST.OBJ.APLICACION / main ----------1",id(main))
    aplicacion=Control(main) # genero la ventana y se la paso a la clase Control()
               ## en el momento que leo esta linea se ejecuta el constructor de Control
    #print("1 CONTROL.PY / INST.OBJ.APLICACION / main ----------1",id(main))
        
    main.mainloop()
