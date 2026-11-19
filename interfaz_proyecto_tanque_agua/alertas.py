import flet as ft
from colores import Colores

def crear_alertas(titulo, descripcion, icono, color):
    return ft.Container(
        padding = 15,
        border_radius = 10,
        bgcolor = Colores["Barra_lateral"],

        content = ft.Row(
            controls = [
                ft.Icon(
                    icono,
                    color = color,
                    size = 25
                ),

                ft.Column(
                    controls = [
                        ft.Text(
                            titulo,
                            color = Colores["Texto"],
                            size = 15,
                            weight = ft.FontWeight.BOLD
                        ),
                        ft.Text(
                            descripcion,
                            color = Colores["Texto_Secundario"],
                            size = 12
                        )
                    ]
                )
            ]
        )
    )

