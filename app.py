# app principal colocada conexion a slqite
from flask import Flask
from flask import render_template, request, redirect, url_for, flash
# Para poder subir archivos y que los muestre
from flask import send_from_directory

import sqlite3 as sql3  # conexion a base de datos
from datetime import datetime  # Para renombrar las imagenes que subamos con la fecha
import os  # Para entrar a la carpeta de imagenes

# FIXME: crear unan clase para poner la conexion independiente a cualquier data base  por ahora la dejare aca - fer
# conexion a base de datos
# ------------------------------------------------

def conexion(path: str) -> bool:
    '''esta funcion se conecta a la base de datos de sqlite teniendo el archivo en local'''
    restul = False
    try:
        # GENERAMOS coneccion con la libreria y un proyecto particular
        conn = sql3.connect(path)
        print("conexion establecida")
        result = True
    except:
        print("no se pudo conectar a al data base")

    return result, conn

# ----------------------------------------------------

app = Flask(__name__)
app.secret_key = 'mysecretkey'

# TODO: falta revisar y crear ruta donde se guardaran las imagenes - fer
carpeta = os.path.join('Static\img')  # Carpeta donde se guardan las imagenes
app.config['CARPETA'] = carpeta

@app.route('/')
def index():
    # ENVIAR PATH Y CONECTARSE
    path = 'db\cinepolis.db'
    result, conn = conexion(path)

    sql = 'SELECT * FROM ASIENTO'
    cursor = conn.cursor()  # Creamos un cursor para poder ejecutar las consultas
    cursor.execute(sql)

    peliculas = cursor.fetchall()  # Obtenemos todos los registros de la tabla peliculas
    print(peliculas)

    conn.commit()
    conn.close()  # no olvidar cerrar siempre la conexion con la db

    respuesta = render_template('peliculas/index.html', peliculas=peliculas)

    return respuesta

# TODO: ------------------------ aca voy ------------------------- fer

@app.route('/signin')
def signin():

    return render_template('peliculas/signin.html')

@app.route('/signup')
def signup():

    return render_template('peliculas/signup.html')

@app.route('/forgetpass')
def forgetpass():

    return render_template('peliculas/forgetpass.html')


@app.route('/uploads/<posterName>')
def uploads(posterName):
    respuesta = send_from_directory(app.config['carpeta'], posterName)
    return respuesta


@app.route('/catalog', methods=['GET', 'POST'])
def catalog():

    return render_template('peliculas/catalog.html')


@app.route('/movies')
def movies():

    return render_template('peliculas/movies.html')


@app.route('/create')
def create():

    return render_template('peliculas/create.html')



if __name__ == '__main__':
    app.run(debug=True)
