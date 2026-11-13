import flet as ft

from colores import Colores

def crear_items(icono, texto, activo = False):
    if activo == True:
        color_fondo = Colores["Turquesa"]
    else:
        color_fondo = None

    return ft.Container(
        padding = 15,
        border_radius = 10,
        bgcolor = color_fondo,

        content = ft.Row(
            controls = [
                ft.Icon(
                    icono,
                    color = Colores["Texto"]
                ),
                ft.Text(
                    texto,
                    color = Colores["Texto"],
                    size = 15
                )
            ]
        )
    )