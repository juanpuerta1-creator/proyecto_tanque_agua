import flet as ft
from flet.controls import border_radius

from colores import Colores

def main(page:ft.Page):
    page.title = "Acuarella - Monitor de tanque de agua"
    page.bgcolor = Colores["Fondo"]
    page.window.width = 1200
    page.window.height = 800
    page.window.min_width = 600
    page.window.min_height = 400

    barra_lateral = ft.Container(
        width = 240,
        bgcolor = Colores["Barra_lateral"],
        padding = 10,
        border_radius = 15
    )

    area_principal = ft.Container(
        expand = True,
        padding = 10
    )

    estructura_principal = ft.Row(
        expand = True,
        spacing = 5,
        controls = [
            barra_lateral,
            area_principal
        ]
    )

    page.add(estructura_principal)

ft.run(main)