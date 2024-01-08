import mysql.connector

# Establecer la conexión
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="datausuarios"
)

# Crear un cursor
cursor = conexion.cursor()

# Consulta SQL para insertar datos
consulta = "INSERT INTO parametros (id, bpm,fr ,spo ,temp ) VALUES (%s, %s,%s, %s,%s)"


# Valores a insertar
valores = (1,2,3,4,5)

# Ejecutar la consulta
cursor.execute(consulta, valores)

# Confirmar los cambios
conexion.commit()

# Cerrar cursor y conexión
cursor.close()
conexion.close()

