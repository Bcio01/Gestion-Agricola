from configuraciones.db import crear_conexion

class UsuariosModelo:
    @staticmethod
    def obtener_usuario(correo, contraseña):
        conexion = crear_conexion()
        if not conexion:
            return None
        cursor = conexion.cursor(dictionary=True)
        query = "SELECT * FROM usuarios WHERE correo=%s AND contraseña=%s"
        cursor.execute(query, (correo, contraseña))
        usuario = cursor.fetchone()
        cursor.close()
        conexion.close()
        return usuario
