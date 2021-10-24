# %%
# import PeliculasDAO
from Conexion import Conexion
from PeliculasDAO import PeliculasDAO

#%%
_id_peli = 2
_img_portada_peli = [123, 345, 456, 345, 345]
_nombre_peli = 'venom'
_sinop_peli = 'xxxx xxxx'
_anio_peli = 2021
_duracion_peli = 120
_formato_peli = '3d'
_catetegoria_peli = '13'
_pais_peli = 'colombia'
_genero_peli = 'terror'
_anadir_link_peli = 'http//:www.google.com'
_id_estado = 23

sql = "INSERT INTO PELICULA (ID_PELICULA, PORTADA, TITULO, SINOPSIS, ANIO, DURACION, FORMATO, CATEGORIA, PAIS, GENERO, VIDEO, ID_ESTADO) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

sql2 = "INSERT INTO PELICULA (ID_PELICULA, PORTADA, TITULO, SINOPSIS, ANIO, DURACION, FORMATO, CATEGORIA, PAIS, GENERO, VIDEO, ID_ESTADO) VALUES ('3', '3002', 'vemon2', 'xxxx xxxx xxxxx', '20212','1202', '3d2', '24','colombia', 'terror', 'youtube.com2', '1')"


var = (_id_peli, _img_portada_peli, _nombre_peli,
       _sinop_peli, _anio_peli, _duracion_peli,
       _formato_peli, _catetegoria_peli,
       _pais_peli, _genero_peli, _anadir_link_peli,
       _id_estado)


movies = PeliculasDAO()
# result = movies.insertar(sql2, var)
result = movies.insertar(sql, var)


print(result)

#%%
# ID_ESTADO	DESCRIPCION 
sql = "INSERT INTO ESTADO (ID_ESTADO, DESCRIPCION) VALUES (?, ?)"

sql2 = "SELECT * FROM ESTADO"
sql3= "UPDATE ESTADO SET DESCRIPCION = 1000 WHERE ID_ESTADO = 2"
sql4 = "SELECT * FROM ESTADO WHERE ID_ESTADO=3"

# -----------------------------------------

sql5 = "INSERT INTO ESTADO (ID_ESTADO, DESCRIPCION) VALUES (9, 'fer')"
# -
var = (1, 'hola')

sql6 = "INSERT INTO PELICULA (ID_PELICULA, PORTADA, TITULO, SINOPSIS, ANIO, DURACION, FORMATO, CATEGORIA, PAIS, GENERO, VIDEO, ID_ESTADO) VALUES ('4', '3002', 'vemon2', 'xxxx xxxx xxxxx', '20212','1202', '3d2', '24','colombia', 'terror', 'youtube.com2', '1')"

var7 = (7, 3002, 'vemon2', 'xxxx xxxx xxxxx', '20212','1202', '3d2', '24','colombia', 'terror', 'youtube.com2', 4)

sql7 = "INSERT INTO PELICULA (ID_PELICULA, PORTADA, TITULO, SINOPSIS, ANIO, DURACION, FORMATO, CATEGORIA, PAIS, GENERO, VIDEO, ID_ESTADO) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"




movies = PeliculasDAO()
# result = movies.insertar(sql2, var)
result = movies.insertar(sql7, var7)  
#result2 = movies.enviar(sql6)

print(result)
# %%

_id_peli = 8
_img_portada_peli = 677899
_nombre_peli = 'venom'
_sinop_peli = 'xxxx xxxx'
_anio_peli = 2021
_duracion_peli = 120
_formato_peli = '3d'
_catetegoria_peli = '13'
_pais_peli = 'colombia'
_genero_peli = 'terror'
_anadir_link_peli = 'http//:www.google.com'
_id_estado = 6

sql8 = "INSERT INTO PELICULA (ID_PELICULA, PORTADA, TITULO, SINOPSIS, ANIO, DURACION, FORMATO, CATEGORIA, PAIS, GENERO, VIDEO, ID_ESTADO) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"


var8 = (_id_peli, _img_portada_peli, _nombre_peli,
       _sinop_peli, _anio_peli, _duracion_peli,
       _formato_peli, _catetegoria_peli,
       _pais_peli, _genero_peli, _anadir_link_peli,
       _id_estado)


movies = PeliculasDAO()
# result = movies.insertar(sql2, var)
result = movies.insertar(sql8, var8)  
#result2 = movies.enviar(sql6)

print(result)

# %%
