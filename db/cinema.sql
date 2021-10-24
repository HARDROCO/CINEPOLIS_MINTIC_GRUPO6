--
-- File generated with SQLiteStudio v3.3.3 on jue. oct. 21 10:36:02 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: carteleras
DROP TABLE IF EXISTS carteleras;
CREATE TABLE carteleras (id INTEGER PRIMARY KEY AUTOINCREMENT, pelicula INTEGER REFERENCES peliculas (id), sala INTEGER REFERENCES salas (id), horaInicio TIME NOT NULL, horaFin TIME NOT NULL, fecha DATE NOT NULL, estado INTEGER REFERENCES estados (id));

-- Table: comentarios
DROP TABLE IF EXISTS comentarios;
CREATE TABLE comentarios (id INTEGER PRIMARY KEY, contenido TEXT NOT NULL, fecha DATETIME NOT NULL, estado INTEGER REFERENCES estados (id), usuario INTEGER REFERENCES usuarios (id));

-- Table: estados
DROP TABLE IF EXISTS estados;
CREATE TABLE estados (id INTEGER PRIMARY KEY AUTOINCREMENT, descripcion VARCHAR (50) NOT NULL);

-- Table: peliculas
DROP TABLE IF EXISTS peliculas;
CREATE TABLE peliculas (id INTEGER PRIMARY KEY AUTOINCREMENT, portada VARCHAR (255) NOT NULL, titulo VARCHAR (50) NOT NULL, duracion INTEGER NOT NULL, genero VARCHAR (50) NOT NULL, clasificacion VARCHAR (50) NOT NULL, formato VARCHAR (50) NOT NULL, sinopsis VARCHAR (100) NOT NULL, estado INTEGER REFERENCES estados (id));

-- Table: perfiles
DROP TABLE IF EXISTS perfiles;
CREATE TABLE perfiles (id INTEGER PRIMARY KEY AUTOINCREMENT, descripcion VARCHAR (50) NOT NULL);

-- Table: reservas
DROP TABLE IF EXISTS reservas;
CREATE TABLE reservas (id INTEGER PRIMARY KEY AUTOINCREMENT, usuario INTEGER REFERENCES usuarios (id), cartelera INTEGER REFERENCES carteleras (id), fecha DATE NOT NULL, silla INTEGER REFERENCES sillas (id), mPago VARCHAR (50) NOT NULL, estado INTEGER REFERENCES estados (id));

-- Table: salas
DROP TABLE IF EXISTS salas;
CREATE TABLE salas (id INTEGER PRIMARY KEY AUTOINCREMENT, descripcion VARCHAR (50) NOT NULL, sillas INTEGER NOT NULL, estado INTEGER REFERENCES estados (id));

-- Table: sillas
DROP TABLE IF EXISTS sillas;
CREATE TABLE sillas (id INTEGER PRIMARY KEY AUTOINCREMENT, sala INTEGER REFERENCES salas (id), fila VARCHAR (5) NOT NULL, numero INTEGER NOT NULL, estado INTEGER REFERENCES estados (id));

-- Table: tickets
DROP TABLE IF EXISTS tickets;
CREATE TABLE tickets (id INTEGER PRIMARY KEY AUTOINCREMENT, tipo VARCHAR (50) NOT NULL, descripcion VARCHAR (50), precio DOUBLE, estado INTEGER REFERENCES estados (id));

-- Table: usuarios
DROP TABLE IF EXISTS usuarios;
CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nombres VARCHAR (50) NOT NULL, apellidos VARCHAR (50) NOT NULL, email VARCHAR (100) NOT NULL, login VARCHAR (50) NOT NULL, password VARCHAR (50) NOT NULL, fec_registro DATE NOT NULL, identificacion VARCHAR (20) NOT NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
