from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from flask import send_from_directory

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('peliculas/index.html')

@app.route('/signin')
def signin():

    return render_template('peliculas/signin.html')

@app.route('/signup')
def signup():

    return render_template('peliculas/signup.html')

@app.route('/forgetpass')
def forgetpass():

    return render_template('peliculas/forgetpass.html')

if __name__ == '__main__':
    app.run(debug=True)