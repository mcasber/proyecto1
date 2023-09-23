from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import datetime
import model
from model import Abmc

#__________VISTA____________________________________________________________________________________
#PASAJE A POO
class Ventanita():
    def __init__(self, window):
        #print("INTERFAZ.PY / CONSTRUCTOR ---------- self",id(self))
        self.objeto_base=Abmc()
        #print("INTERFAZ.PY / CONSTRUCTOR / SELF INSTANCIACION OBJETO BASE ---------- self.objeto_base",id(self.objeto_base))
        
        self.master = window
        #print("INTERFAZ.PY / CONSTRUCTOR ---------- self.master",id(self.master))
        self.master.geometry("600x600")
        self.master.title("TP Mariano Castelli")

        self.titulo = Label(self.master, text="App para control de ingresos/egresos al: ")
        self.titulo.grid(row=0, column=1, sticky="e")

        self.fecha_hoy = Label(self.master, text=(datetime.datetime.today().strftime("%d/%m/%y")))
        self.fecha_hoy.grid(row=0, column=10, sticky="e")

        # LABEL Y ENTRY 
        self.fecha = Label(self.master, text="Fecha:")
        self.fecha.grid(row=2, column=0, sticky="e")
        self.detalle = Label(self.master, text="Detalle:")
        self.detalle.grid(row=3, column=0, sticky="e")
        self.importe = Label(self.master, text="Importe:")
        self.importe.grid(row=4, column=0, sticky="e")
        self.id_baja = Label(self.master, text="Ingrese el id a dar de baja:")
        self.id_baja.grid(row=5, column=0, sticky="e")
        self.id_modificar = Label(self.master, text="Ingrese el id a modificar:")
        self.id_modificar.grid(row=9, column=0, sticky="e")
        self.importe_modificar = Label(self.master, text="Ingrese el importe a modificar:")
        self.importe_modificar.grid(row=10, column=0, sticky="e")
        self.id_consultar = Label(self.master, text="Ingrese el id a consultar:")
        self.id_consultar.grid(row=11, column=0, sticky="e")
        
        #ESTO ES PARA MOSTRAR LOS MENSAJES
        self.mensaje = Label(self.master, text="MENSAJE: ")
        self.mensaje.grid(row=12, column=0, sticky="e")
        self.prueba = Label(self.master, text="")
        self.prueba.grid(row=12, column=1, sticky="e")

        #VARIABLES PARA LOS CAMPOS ENTRY
        self.var_fecha = StringVar() 
        self.var_detalle = StringVar()
        self.var_importe = StringVar()
        self.var_id_baja = StringVar()
        self.var_id_modificar = StringVar()
        self.var_importe_modificar = StringVar()
        self.var_id_consultar = StringVar()

        self.entrada_fecha = DateEntry(self.master, width=25, selectmode="day", textvariable=self.var_fecha, date_pattern='dd/MM/yyyy')
        self.entrada_fecha.grid(row=2, column=1)

        self.entrada_detalle = Entry(self.master, textvariable=self.var_detalle, width=25)
        self.entrada_detalle.grid(row=3, column=1)

        self.entrada_importe = Entry(self.master, textvariable=self.var_importe, width=25)
        self.entrada_importe.grid(row=4, column=1)

        self.entrada_id_baja = Entry(self.master, textvariable=self.var_id_baja, width=10)
        self.entrada_id_baja.grid(row=5, column=1)

        self.entrada_id_modificar = Entry(self.master, textvariable=self.var_id_modificar, width=10)
        self.entrada_id_modificar.grid(row=9, column=1)
        self.entrada_importe_modificar = Entry(self.master, textvariable=self.var_importe_modificar, width=10)
        self.entrada_importe_modificar.grid(row=10, column=1)

        self.entrada_id_consultar = Entry(self.master, textvariable=self.var_id_consultar, width=10)
        self.entrada_id_consultar.grid(row=11, column=1)

        #TREEVIEW
        self.tree = ttk.Treeview(self.master) # creo el treeview dentro de master
        self.tree["columns"] = ("col1", "col2", "col3")  # creo una lista donde defino la cantidad de columnas que voy a utilizar
        self.tree.column("#0", width=50, minwidth=50, anchor="w") # defino las propiedades de las columnas
        self.tree.column("col1", width=80, minwidth=80, anchor="w")
        self.tree.column("col2", width=80, minwidth=80, anchor="w")
        self.tree.column("col3", width=80, minwidth=80, anchor="w")
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Fecha")
        self.tree.heading("col2", text="Detalle")
        self.tree.heading("col3", text="Importe")
        self.tree.grid(column=0, row=20, columnspan=4)

        """PRUEBA CON RETURN
        def alta_base_datos():
            resultado=model.alta_base_datos(var_fecha,var_detalle,var_importe,tree,prueba)
            print(resultado)
        """
        #BOTONES
        boton_alta = Button(self.master, text="Alta", 
                            command=lambda:self.objeto_base.alta_base_datos
                            (self.var_fecha,self.var_detalle,self.var_importe,self.tree,self.prueba))
        boton_alta.grid(row=4, column=2)

        boton_baja = Button(self.master, text="Baja", 
                            command= lambda:self.objeto_base.baja_base_datos(self.var_id_baja, self.tree))
        boton_baja.grid(row=5, column=2)

        boton_modificar=Button(self.master, text="Modificar", 
                               command=lambda:self.objeto_base.modificar_importe(self.var_importe_modificar,self.var_id_modificar,self.tree))
        boton_modificar.grid(row=10, column=2)

        boton_consultar_id = Button(self.master, text="Consultar Id", 
                                    command=lambda:self.objeto_base.consultar_id(self.var_id_consultar,self.tree))
        boton_consultar_id.grid(row=11, column=2)
