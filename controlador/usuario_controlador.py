from modelo.usuarios_modelo import UsuariosModelo

class UsuarioControlador:
    @staticmethod
    def login(correo, contraseña):
        usuario = UsuariosModelo.obtener_usuario(correo, contraseña)
        return usuario
