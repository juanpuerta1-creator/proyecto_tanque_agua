import flet as ft
from flet.controls import alignment

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

def cuenta_usuario(nombre, rol, iniciales_nombre):
    return ft.Container(
        padding = 15,
        border_radius = 10,

        content = ft.Row(
            controls = [
                ft.Container(
                    width = 40,
                    height = 20,
                    bgcolor = Colores["Barra_Lateral"],
                    alignment = ft.Alignment.CENTER,

                    content = ft.Text(
                        iniciales_nombre,
                        color = Colores["Fondo"],
                        weight = ft.FontWeight.BOLD,
                    )
                ),
                ft.Column(
                    controls = [
                        ft.Text(
                            nombre,
                            color = Colores["Texto"],
                            weight = ft.FontWeight.BOLD,
                            size = 15
                        ),
                        ft.Text(
                            rol,
                            color = Colores["Texto_Secundario"],
                            size = 10
                        )
                    ]
                )
            ]
        )
    )
