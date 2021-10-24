# clase para crear conexiones con la data base

# conexion a base de datos
# ------------------------------------------------
import sqlite3 as sql3
import os


class Conexion():
    # ENVIAR PATH Y CONECTARSE
    path = 'db\DB_Cinepolis.db'
    sql = ""

    def __init__(self):
        return

    def conectar(self) -> sql3.Connection:
        '''esta funcion se conecta a la base de datos de sqlite teniendo el archivo en local y devuelve un objeto tipo conexion para crear cursor y ejecutar querys'''
        result = False
        try:
            # GENERAMOS coneccion con la libreria y un proyecto particular
            conn = sql3.connect(self.path)
            print("conexion establecida")
            conn.row_factory = sql3.Row # trae los datos como diccionarios
            result = True
        except:
            print("no se pudo conectar a la data base")

        return conn


print()