# clase para crear conexiones con la data bate 


# FIXME: crear unan clase para poner la conexion independiente a cualquier data base  por ahora la dejare aca - fer
# conexion a base de datos
# ------------------------------------------------

class conexion():
    def __init__(self):
        return

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


    # ENVIAR PATH Y CONECTARSE
    path = 'db\cinepolis.db'
    result, conn = conexion(path)






