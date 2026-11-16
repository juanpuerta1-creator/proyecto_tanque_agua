import flet as ft
from PIL.ImageColor import colormap

from colores import Colores

def crear_tarjeta(titulo, cantidad, icono, color):
    return ft.Container(
        padding = 15,
        border_radius = 10,
        bgcolor = Colores["Barra_lateral"],

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
                            size = 12
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