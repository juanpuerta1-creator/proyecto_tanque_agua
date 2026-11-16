import flet as ft
from colores import Colores
from barra_lateral import crear_items, cuenta_usuario
from encabezado import crear_encabezado, encabezado_principal

def main(page:ft.Page):
    page.title = "Acuarella - Monitor de tanque de agua"
    page.bgcolor = Colores["Fondo"]
    page.window.width = 1200
    page.window.height = 800
    page.window.min_width = 600
    page.window.min_height = 400

    encabezado = crear_encabezado()
    encabezado_2 = encabezado_principal()

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
                ft.Text(
                    "MENU PRINCIPAL",
                    color = Colores["Texto_Secundario"],
                    size = 12,
                    weight = ft.FontWeight.BOLD
                ),
                crear_items(ft.Icons.DASHBOARD, "Vista general", True),
                crear_items(ft.Icons.STORAGE, "Tanques"),
                crear_items(ft.Icons.SHOW_CHART, "Historial"),
                crear_items(ft.Icons.NOTIFICATIONS, "Alertas"),

                ft.Container(
                    expand = True
                ),
                cuenta_usuario("Juan Puerta", "Administrador Principal", "JP")
            ]
        )
    )

    area_principal = ft.Container(
        expand = True,
        padding = 10,

        content = ft.Column(
            controls = [
                encabezado_2
            ]
        )
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