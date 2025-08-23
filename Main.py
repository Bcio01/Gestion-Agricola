import flet as ft
from vistas.login import LoginVista

from configuraciones.db import crear_conexion

def main(page: ft.Page):
    page.title = "Gestion Agregicola"
    # Dimensiones de la aplicacion
    page.window.width = 500
    page.window.height = 600
    # Centrando la aplicacion al iniciarla
    page.window.center()
    # Muestra la vista login
    conexion = crear_conexion()

    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SHOW TABLES;")
        tablas = cursor.fetchall()
        print("Tablas en la BD:", tablas)
        cursor.close()
        conexion.close()
    
    # Manejo de rutas
    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(LoginVista())
            

        page.update()

    page.on_route_change = route_change
    page.go("/")  # Inicia en login

ft.app(target=main)
