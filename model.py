import sqlite3
import re
from observador import Sujeto
#__________MODELO__________________________________________________________________________________________
class Abmc(Sujeto):
    def __init__(self,):
        #print("MODEL.PY / CONSTRUCTOR ---------- self",id(self))
        con = sqlite3.connect('basetp.db')
        cursor = con.cursor() # esto me va a permitir poder agregar info a esa base de datos
        
        sql = "CREATE TABLE IF NOT EXISTS gastos(id integer PRIMARY KEY AUTOINCREMENT, fecha datetime, detalle text, importe integer)" 
                
        cursor.execute(sql) # le estoy diciendo que tome esta instruccion ---->(sql)
        con.commit() # y que la ejecute

    def conexion(self,):
        con = sqlite3.connect('basetp.db')
        return con

    # FUNCION PARA ACTUALIZAR TREE / AHORA ES METODO
    def funcion_actualizar_tree(self, tree):
        #primero lo vacio
        records = tree.get_children()
        for element in records:
            tree.delete(element)
        
        #cargo todo desde la bd
        sql = "SELECT * FROM gastos ORDER BY id ASC"
        con=self.conexion()
        cursor=con.cursor()
        datos=cursor.execute(sql)

        resultado = datos.fetchall()
        for fila in resultado:
            #print(fila)
            tree.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))

    # FUNCION PARA INGRESAR DATOS EN BD
    def alta_base_datos(self, var_fecha,var_detalle,var_importe,tree,prueba):
        #print("MODEL.PY / METODO ALTA ---------- self",id(self))

        cadena = var_detalle.get() 
        patron="^[A-Za-záéíóú]*$"  
        
        if(re.match(patron, cadena)):
            
            con = self.conexion()
            cursor = con.cursor()
            
            #PATRON OBSERVADOR
            self.notificar(var_fecha.get(),var_detalle.get(), var_importe.get())

            print(var_fecha.get(),var_detalle.get(),var_importe.get())

            sql_query = f"INSERT INTO gastos(fecha, detalle, importe) VALUES('{var_fecha.get()}','{var_detalle.get()}','{var_importe.get()}')"
            
            cursor.execute(sql_query) # ejecuto sql_query con la data que le estoy pasando
            con.commit()# y que la ejecute
            con.close() # y que la cierre - ver si esto es necesario, parece bueno para evitar errores de conexion post
            
            self.funcion_actualizar_tree(tree)
            prueba.config(text="") #si carga el detalle vacio el campo prueba
            var_fecha.set("")
            var_detalle.set("")
            var_importe.set("")
            #return "salio todo bien"
        else:
            print("Error en campo Detalle")
            prueba.config(text="CARACTER NO VALIDO en DETALLE")

    # FUNCION PARA BORRAR POR ID EN LA BD
    def baja_base_datos(self, var_id_baja, tree): 
        con = self.conexion()
        cursor = con.cursor()
        
        print(var_id_baja)
        
        sql_query = f"DELETE from gastos where id='{var_id_baja.get()}'" 
                
        cursor.execute(sql_query)
        con.commit()
        con.close()

        self.funcion_actualizar_tree(tree)
        var_id_baja.set("")

    # FUNCION PARA ACTUALIZAR DATOS EN LA BD ## por el momento modifico solo el importe
    def modificar_importe(self, var_importe_modificar,var_id_modificar,tree):
        con = self.conexion()
        cursor = con.cursor()
            
        print(var_importe_modificar,var_id_modificar)

        sql_query = f"UPDATE gastos SET importe='{var_importe_modificar.get()}' WHERE id='{var_id_modificar.get()}'"
    
        cursor.execute(sql_query)
        con.commit()
        con.close()

        self.funcion_actualizar_tree(tree)
        var_id_modificar.set("")
        var_importe_modificar.set("")
        
    # FUNCION PARA SELECCIONAR / CONSULTAR POR ID
    def consultar_id(self, var_id_consultar,tree):
        con = self.conexion()
        cursor = con.cursor()
        
        print(var_id_consultar)
        
        sql_query = f"SELECT * FROM gastos WHERE id ='{var_id_consultar.get()}'" 
        
        cursor.execute(sql_query)
        con.commit()     
        
        self.funcion_actualizar_tree(tree)
        var_id_consultar.set("")

        consulta= cursor.fetchall()
        print(consulta)


