import pandas as pd
import numpy as np
from model import Abmc

con=Abmc.conexion('basetp.db')
cursor=con.cursor()
sql = "SELECT * FROM gastos ORDER BY id ASC"
datos=cursor.execute(sql)

df=pd.DataFrame(datos)
#print("DATAFRAME\n", df)
print("\nShape:", df.shape)
print("Filas:", len(df.index))
print("Columnas:", len(df.columns))

print("\nESTADISTICAS")
print(df[3].describe())
        #aca indico la columna


"""
print("\nMedia")
print(df[3].mean())
print("\nMediana")
print(df[3].median())
print("\nValores no nulos")
print(df[3].count())
print("\nValores máximos")
print(df[3].max())
print("\nValores mínimos")
print(df[3].min())
print("\nDesvío Estándar")
print(df[3].std())
"""