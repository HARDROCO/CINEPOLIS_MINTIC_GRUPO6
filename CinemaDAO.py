# Clase creada para hacer consultas a la base de datos utilizando el concepto de MVC

import sqlite3 as sql3
from datetime import datetime
import os
from Conexion import Conexion


class CinemaDAO():
    # constructor de clase
    def __init__(self):
        return

# funcion para consultar tablas de la database sin filtrar o para crear nuevas tablas
    def select_table(self, sql: str) -> tuple:
        '''Esta funcion se conecta a la base de datos de sqlite recibiendo un query de sql "SELECT * FROM tabla1", y consulta una tabla completa de la database sin usar filtros como el WHERE'''

        print("ejecutando query...")
        resp = False

        try:
            # enviar conexiona  DB
            conexion = Conexion()  # creamos el objeto
            conn = conexion.conectar()  # enviamos conexion

            # si se conecta a DB
            if conn != None:
                cursor = conn.cursor()  # Creamos un cursor
                cursor.execute(sql)  # enviar consulta
                result = cursor.fetchall()  # Obtenemos todos los registros
            resp = True
        except:
            conn.rollback()  # si hay un error, se deshace la transaccion
            print("no se pudo conectar a la data base")

        conn.commit()
        conn.close()  # no olvidar cerrar siempre la conexion con la db

        return result


# funcion para filtar, insertar y borrar datos en la database

    def filter_table(self, sql: str, var: tuple) -> tuple:
        '''Esta funcion se conecta a la base de datos de sqlite y envia una consulta que puede ser del tipo "SELECT col1 FROM tabla1  WHERE col1 = valor y devuelve todas ls filas resultado'''

        print("ejecutando query")
        resp = False

        try:
            # enviar conexiona  DB
            conexion = Conexion()  # creamos el objeto
            conn = conexion.conectar()  # enviamos conexion

            # si se conecta a DB
            if conn != None:
                cursor = conn.cursor()  # Creamos un cursor
                print(sql,var)
                cursor.execute(sql, var)  # enviar consulta
                #cursor.execute("SELECT * FROM usuarios where correo = 'g@yahoo.com'")
                #Esto no puede ir aqui, porque aún no se a ejecutado el commit
                #result = cursor.fetchall()  # Obtenemos todos los registros
                
            resp = True
        except:
            conn.rollback()  # si hay un error, se deshace la transaccion
            print("no se pudo conectar a la data base cinemaDAO")

        conn.commit()
        result = cursor.fetchone()
        #print(result["nombre"])
        conn.close()  # no olvidar cerrar siempre la conexion con la db
        
        return result


# funcion para filtar, insertar y borrar datos en la database

    def InsertDrop_table(self, sql: str, var: tuple) -> bool:
        '''Esta funcion se conecta a la base de datos de sqlite y envia una consulta que modifica la tabla puede ser "UPDATE" o "DROP" usando filtros que puede ser del tipo "UPDATE col1 FROM tabla1  WHERE col1 = valor" y devuelve un bolean true o false indicando el exito o el fracaso de la query
        Esta funcion recibe los valores del filtro como tuplas var =(2,3) o var = (2,) que sera reemplazados por los espacios de ? en la consulta
        "UPDATE col1 FROM tabla1  WHERE col1 = ? "'''

        print("ejecutando query...")
        resp = False

        try:
            # enviar conexiona  DB
            conexion = Conexion()  # creamos el objeto
            conn = conexion.conectar()  # enviamos conexion

            # si se conecta a DB
            if conn != None:
                cursor = conn.cursor()  # Creamos un cursor
                cursor.execute(sql, var)  # enviar consulta
            resp = True
        except:
            conn.rollback()  # si hay un error, se deshace la transaccion
            print("no se pudo conectar a la data base")

        conn.commit()
        conn.close()  # no olvidar cerrar siempre la conexion con la db

        return resp


# funcion para filtar, insertar y borrar datos en la database


    def InsertDrop_test(self, sql: str) -> bool:
        '''Esta funcion se conecta a la base de datos de sqlite y envia una consulta que modifica la tabla puede ser "UPDATE" o "DROP" no requiere valores de filtro solo la query, se creo para testear codigo sql antes de probar con el servidor, devuelve un boolean'''

        print("ejecutando query...")
        resp = False

        try:
            # enviar conexiona  DB
            conexion = Conexion()  # creamos el objeto
            conn = conexion.conectar()  # enviamos conexion

            # si se conecta a DB
            if conn != None:
                cursor = conn.cursor()  # Creamos un cursor
                cursor.execute(sql)  # enviar consulta
            resp = True
        except:
            conn.rollback()  # si hay un error, se deshace la transaccion
            print("no se pudo conectar a la data base")

        conn.commit()
        conn.close()  # no olvidar cerrar siempre la conexion con la db

        return resp
