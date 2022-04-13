import pymysql
import json 

def generateConexion(server, userName, userPassword, nameDb):
    try:
        conexion = pymysql.connect(
            host=server,
            user=userName,
            password=userPassword,
            db=nameDb
        )
        return conexion;
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as error:
        return None;
        

def getData(tableName):
    try:
        conexion = generateConexion('localhost', 'root', '12345', 'animales');
        with conexion.cursor() as cursor:
            query = f"SELECT * FROM {tableName};"

            cursor.execute(query)

            filas = cursor.fetchall()

            #crear estructuras para almacenar la data
            datosDePerros = []

            for fila in filas:
                datoDePerro = []
                datoDePerro.append(fila[0])
                datoDePerro.append(fila[1])
                datoDePerro.append(fila[2])
                datoDePerro.append(fila[3])

                datosDePerros.append(datoDePerro)

            return datosDePerros;
    finally:
        conexion.close()  
    return None;

# select * from where = ?

def getDataById(tableName, id):
    try:
        conexion = generateConexion('localhost', 'root', '12345', 'animales');
        with conexion.cursor() as cursor:
            query = f"SELECT * FROM {tableName} WHERE id = %s;"

            cursor.execute(query, (id))

            filas = cursor.fetchall()

            datoDePerro = []

            for fila in filas:
                diccionario = { 'id' : fila[0],
                                'nombre' : fila[1],
                                'raza' : fila[2],
                                'edad' : fila[3] }
                '''
                datoDePerro.append(fila[0])
                datoDePerro.append(fila[1])
                datoDePerro.append(fila[2])
                datoDePerro.append(fila[3])
                '''

            return diccionario;
    finally:
        conexion.close()  
    return None;



datosDiccionario = getDataById('perro', 2)

jsonData = json.dumps(datosDiccionario, indent=5)

print(jsonData)

