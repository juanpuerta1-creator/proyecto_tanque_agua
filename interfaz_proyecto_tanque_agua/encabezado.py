import flet as ft
from flet.controls import border

from colores import Colores

def crear_encabezado():
    encabezado = ft.Row(
        controls = [
            ft.Image(
              src = "assets/Logo.png",
                width = 80,
                height = 80,
                fit = ft.BoxFit.CONTAIN
            ),
            ft.Text("Acuarella", size = 20, weight = ft.FontWeight.BOLD, color = Colores["Texto"])
        ],
        spacing = 5,
        alignment = ft.MainAxisAlignment.CENTER
    )
    return encabezado

def encabezado_principal():
        encabezado_2 = ft.Row(
            controls=[
                ft.Column(
                    controls = [
                        ft.Text(
                            "Monitoreo del tanque",
                            size = 25,
                            color = Colores["Texto"]
                        ),

                        ft.Text(
                            "Tanque principal",
                            size = 15,
                            color = Colores["Texto_Secundario"]
                        )
                    ],
                    spacing = 5,
                    alignment = ft.MainAxisAlignment.CENTER
                ),

                ft.Container(
                    expand = True
                ),

                ft.Image(
                    src = "assets/IconoBanner.png",
                    width = 100,
                    height = 100,
                    fit = ft.BoxFit.CONTAIN
                )
            ],
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment = ft.CrossAxisAlignment.CENTER
        )
        return encabezado_2