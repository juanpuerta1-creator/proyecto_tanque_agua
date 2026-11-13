import flet as ft
from colores import Colores
from barra_lateral import crear_items
from encabezado import crear_encabezado

def main(page:ft.Page):
    page.title = "Acuarella - Monitor de tanque de agua"
    page.bgcolor = Colores["Fondo"]
    page.window.width = 1200
    page.window.height = 800
    page.window.min_width = 600
    page.window.min_height = 400

    encabezado = crear_encabezado()

    barra_lateral = ft.Container(
        width = 240,
        bgcolor = Colores["Barra_lateral"],
        padding = 10,
        border_radius = 15,
        content = ft.Column(
            controls = [
                encabezado,
                ft.Divider(
                    color = Colores["Fondo"],
                    thickness = 2
                ),
                crear_items(ft.Icons.DASHBOARD, "Vista general"),
                crear_items(ft.Icons.STORAGE, "Tanques"),
                crear_items(ft.Icons.SHOW_CHART, "Historial"),
                crear_items(ft.Icons.NOTIFICATIONS, "Alertas")
            ]
        )
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

    items = crear_items(
        ft.Icons.DASHBOARD,
        "Vista general"
    )
    page.add(items)


ft.run(main)