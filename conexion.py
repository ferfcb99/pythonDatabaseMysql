import pymysql

try:

    conexion = pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        db='animales'
    )
    print("Conexion exitosa")

    try:
        with conexion.cursor() as cursor:

            #crear la consulta o query
            cursor.execute("SELECT * FROM perro;")

            datosDePerros = cursor.fetchall()

            for datoDePerro in datosDePerros:
                print(datoDePerro)
    
    finally:
        conexion.close()


except(pymysql.err.OperationalError, pymysql.err.InternalError) as error:
    print('Ocurrio un error', error)

