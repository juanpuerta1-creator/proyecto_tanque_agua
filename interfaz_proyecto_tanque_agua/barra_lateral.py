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

def cuenta_usuario(nombre, rol, iniciales_nombre):
    return ft.Container(
        padding = 10,
        border_radius = 15,
        bgcolor = Colores["Barra_lateral"],

        content = ft.Row(
            controls = [
                ft.Container(
                    width = 40,
                    height = 40,
                    border_radius = 50,
                    bgcolor = Colores["Fondo"],
                    alignment = ft.Alignment.CENTER,

                    content = ft.Image(
                        src = "assets/Perfil.png",
                        width = 40,
                        height = 40,
                        fit = ft.BoxFit.CONTAIN
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
                    ],
                    spacing = 2
                )
            ]
        )
    )