from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from flask import send_from_directory

app = Flask(__name__)

#Listas de prueba
lista_peliculas = ["pelicula1", "pelicula2", "pelicula3"]
lista_usuarios = ["Juan", "Pedro", "Maria"]

sesion_iniciada = False

@app.route('/', methods=['GET'])
def index():

    return render_template('peliculas/index.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template('peliculas/signin.html')
    else:
        sesion_iniciada = True
        return redirect(url_for('index'))
    

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('peliculas/signup.html')
    else:
        return redirect(url_for('signin'))

@app.route('/forgetpass', methods=['GET', 'POST'])
def forgetpass ():

    return render_template('peliculas/forgetpass.html')

@app.route('/cartelera/', methods=['GET'])
def cartelera():
    return render_template('peliculas/cartelera.html')

@app.route('/pelicula/<id_pelicula>', methods=['GET'])
def pelicula(id_pelicula):
    if id_pelicula in lista_peliculas:
        return render_template('peliculas/pelicula.html')
    else:
        return redirect(url_for('cartelera'))

@app.route('/perfil/<id_usuario>', methods=['GET'])
def perfil(id_usuario):
    if id_usuario in lista_usuarios:
        return render_template('peliculas/perfil.html')
    else:
        return redirect(url_for('signin'))

@app.route('/comidas/', methods=['GET'])
def comidas():
    return render_template('peliculas/comidas.html')

@app.route('/proximamente/', methods=['GET'])
def proximamente():
    return render_template('peliculas/proximamente.html')

if __name__ == '__main__':
    app.run(debug=True)