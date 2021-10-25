from flask import Flask
from flask import render_template, request, redirect, url_for, flash

from datetime import datetime  # Para renombrar las imagenes que subamos con la fecha
import os  # Para entrar a la carpeta de imagenes

# Librerias para crear conexion
from Conexion import Conexion
from CinemaDAO import CinemaDAO

#Libreria para cifrar el password
import hashlib

# TODO: ya quedaron las clases de conexion y consultas creadas para enviar una consutla filtrada debe hacerse con una tupla y para evitar insercion de codigo utilizar ? en el puesto del valor en sqlite
app = Flask(__name__)

# Listas de prueba
lista_peliculas = ["pelicula1", "pelicula2", "pelicula3"]
lista_usuarios = ["Juan", "Pedro", "Maria"]

sesion_iniciada = False


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    global sesion_iniciada
    if request.method == 'GET':
        return render_template('signin.html')
    else:
        sesion_iniciada = True
        #Código para loguearse
         #**************************************
        email = request.form['email']
        password = request.form['password']
        enc = hashlib.sha256(password.encode())
        pass_enc = enc.hexdigest()

        # instruccion sql para enviar info a la DB
        sql = "SELECT * FROM usuarios WHERE correo = ? and contrasena = ?"

        # tupla de valores que se enviaran a la DB
        var = (email,pass_enc,)
        
        # instanciando objeto DAO
        movies = CinemaDAO()
        result = movies.filter_table(sql, var)
        #print(result["correo"], result["contrasena"])  # impresion de resultado de la insercion
        print(result)
        if result == None:
            print("Usuario, no autorizado")
            return redirect(url_for('index'))
        else:
            #if (result["correo"] == email and result["contrasena"] == pass_enc):
            return redirect(url_for('cartelera'))
    


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    global sesion_iniciada
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        #**************************************
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        enc = hashlib.sha256(password.encode())
        pass_enc = enc.hexdigest()

        _id_estado = 2

        # instruccion sql para enviar info a la DB
        sql = "INSERT INTO usuarios (nombre, correo,contrasena, id_rol) VALUES (?, ?, ?, ?)"

        # tupla de valores que se enviaran a la DB
        var = (nombre, email, pass_enc, _id_estado)

        # instanciando objeto DAO
        movies = CinemaDAO()
        result = movies.InsertDrop_table(sql, var)
        print(result)  # impresion de resultado de la insercion
        return render_template('signin.html')


@app.route('/signout', methods=['POST'])
def signout():
    global sesion_iniciada
    sesion_iniciada = False
    return redirect(url_for('index'))


@app.route('/forgot', methods=['GET', 'POST'])
def forgot():

    return render_template('forgot.html')


@app.route('/cartelera/', methods=['GET'])
def cartelera():
    return render_template('cartelera.html')


@app.route('/proximamente/', methods=['GET'])
def proximamente():
    return render_template('proximamente.html')


@app.route('/pelicula/', methods=['GET'])
def pelicula():
    return render_template('pelicula.html')

# @app.route('/pelicula/<id_pelicula>', methods=['GET'])
# def pelicula(id_pelicula):
#     if id_pelicula in lista_peliculas:
#         return render_template('pelicula.html')
#     else:
#         return redirect(url_for('cartelera'))


@app.route('/perfil', methods=['GET'])
def perfil():
    return render_template('perfil.html')

# @app.route('/perfil/<id_usuario>', methods=['GET'])
# def perfil(id_usuario):
#     if id_usuario in lista_usuarios:
#         return render_template('perfil.html')
#     else:
#         return redirect(url_for('signin'))


@app.route('/comidas/', methods=['GET'])
def comidas():
    return render_template('comidas.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


@app.route('/index-admin')
def indexadmin():
    return render_template('admin/index-admin.html')


@app.route('/404')
def notfound():
    return render_template('admin/404.html')


@app.route('/edit-user')
def edituser():
    return render_template('/admin/edit-user.html')


@app.route('/add-item')
def additem():
    return render_template('/admin/add-item.html')


@app.route('/users')
def users():
    return render_template('/admin/users.html')


@app.route('/reviews')
def reviews():
    return render_template('/admin/reviews.html')


@app.route('/catalog')
def catalog():
    return render_template('/admin/catalog.html')


@app.route('/signin-admin')
def signinadmin():
    return render_template('/admin/signin-admin.html')


@app.route('/signup-admin')
def signupadmin():
    return render_template('/admin/signup-admin.html')


@app.route('/forgot-admin')
def forgotadmin():
    return render_template('/admin/forgot-admin.html')


@app.route('/comments')
def comments():
    return render_template('/admin/comments.html')


@app.route('/storestado', methods=['POST'])
def storestado():
    return render_template('/admin/comments.html')

# --------------------------------------------------------------
# metodo para enviar datos de peliculas a la base de datos


@app.route('/storemovie', methods=['GET', 'POST'])
def storemovie():

    if request.method == 'POST':
        # _id_peli = request.form.get('id_peliculas', False)

        # variables que se captiuran del html para enviar a la base de datos
        _id_peli = request.form['id_peliculas']
        _img_portada_peli = request.form['form__img-upload']
        _nombre_peli = request.form['titulo_pelicula']
        _sinop_peli = request.form['Sinopsis']
        _anio_peli = request.form['anio_pelicula']
        _duracion_peli = request.form['duracion_pelicula']
        _formato_peli = request.form['formato_pelicula']
        _catetegoria_peli = request.form['categoria_pelicula']
        _pais_peli = request.form['pais_pelicula']
        _genero_peli = request.form['genero_pelicula']
        _anadir_link_peli = request.form['anadir_link_pelicula']
        # TODO: AJUSTAR VALOR A BD RELACIONAL
        _id_estado = 1

        # instruccion sql para enviar info a la DB
        sql = "INSERT INTO PELICULA (ID_PELICULA, PORTADA, TITULO, SINOPSIS, ANIO, DURACION, FORMATO, CATEGORIA, PAIS, GENERO, VIDEO, ID_ESTADO) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

        # tupla de valores que se enviaran a la DB
        var = (_id_peli, _img_portada_peli, _nombre_peli,
               _sinop_peli, _anio_peli, _duracion_peli,
               _formato_peli, _catetegoria_peli,
               _pais_peli, _genero_peli, _anadir_link_peli,
               _id_estado)

        # instanciando objeto DAO
        movies = CinemaDAO()
        result = movies.InsertDrop_table(sql, var)
        print(result)  # impresion de resultado de la insercion

    else:
        print("NO SE ENVIO LA QUERY")

    return render_template('/admin/catalog.html')


if __name__ == '__main__':
    app.run(debug=True)
