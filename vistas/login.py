import flet as ft
from controlador.usuario_controlador import UsuarioControlador

class LoginVista(ft.View):
    def __init__(self, route="/"):
        super().__init__(route)

        self.usuario = ft.TextField(label="Correo", width=300)
        self.contraseña = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)
        self.mensaje = ft.Text("", color="red")

        boton_login = ft.ElevatedButton("Iniciar Sesión", on_click=self.iniciar_sesion)

        self.controls = [
            ft.Column(
                [
                    ft.Text("Inicio de sesión", size=20, weight="bold"),
                    self.usuario,
                    self.contraseña,
                    boton_login,
                    self.mensaje,
                ],
                alignment="center",
                horizontal_alignment="center",
            )
        ]

    def iniciar_sesion(self, e):
        usuario = UsuarioControlador.login(self.usuario.value, self.contraseña.value)
        if usuario:
        #    self.page.go("/")
            self.mensaje.value = "Bienvenido Al sistema"
        else:
            self.mensaje.value = "Usuario o contraseña incorrectos"
            self.mensaje.color = "red"
        self.update()
