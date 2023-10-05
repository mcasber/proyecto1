import pandas as pd
import numpy as np
from model import Abmc

con=Abmc.conexion('basetp.db')
cursor=con.cursor()
sql = "SELECT * FROM gastos ORDER BY id ASC"
datos=cursor.execute(sql)

df=pd.DataFrame(datos)
#print(df.head(2))
print(df.info())

df[3] = df[3].replace('', '0') # Reemplazar cadenas vacías con 0
df[3] = df[3].astype(float)
print(df.info())

df["Requiere"] = df[3].apply(lambda x: "Aprobar" if x > 100 else "No aprobar")
print(df.head(2))