import flet as ft

from colores import Colores

def crear_items(icono, texto):
    return ft.Container(
        padding = 15,
        border_radius = 10,
        bgcolor = Colores["Turquesa"],

        content = ft.Row(
            controls = [
                ft.Icon(
                    icono,
                    color = Colores["Texto"],
                ),
                ft.Text(
                    texto,
                    color = Colores["Texto"],
                    size = 15
                )
            ]
        )
    )

