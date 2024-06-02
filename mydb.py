import mysql.connector
from mysql.connector import Error

try:
    # Conectar a la base de datos
    dataBase = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='Admin8919*',
        auth_plugin='mysql_native_password'
    )

    if dataBase.is_connected():
        print("Conexión exitosa a MySQL")

        # Preparar un cursor
        cursorObject = dataBase.cursor()

        # Crear la base de datos
        cursorObject.execute("CREATE DATABASE crm_rod")
        print("Base de datos creada exitosamente")

except Error as e:
    print(f"Error al conectar a MySQL: {e}")

finally:
    if dataBase.is_connected():
        cursorObject.close()
        dataBase.close()
        print("Conexión a MySQL cerrada")
