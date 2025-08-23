import mysql.connector
from mysql.connector import Error

def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",       
            user="root",           
            password="admin123", 
            database="gestion_agricola"
        )
        if conexion.is_connected():
            print("Se conecto correctamente a MySQL")
            return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None
