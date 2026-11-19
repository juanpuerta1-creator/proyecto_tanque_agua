import flet as ft
from flet.controls import border_radius

from colores import Colores

def crear_tarjeta(titulo, cantidad, icono, color):
    return ft.Container(
        padding = 15,
        border_radius = 10,
        bgcolor = Colores["Barra_lateral"],
        expand = True,

        content = ft.Column(
            controls = [
                ft.Row(
                    controls = [
                        ft.Text(
                            titulo,
                            color = Colores["Texto_Secundario"],
                            size = 12
                        ),
                        ft.Icon(
                            icono,
                            color = color,
                        )
                    ],
                    alignment = ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Text(
                    cantidad,
                    color = Colores["Texto"],
                    size = 25,
                    weight = ft.FontWeight.BOLD
                )
            ]
        )
    )