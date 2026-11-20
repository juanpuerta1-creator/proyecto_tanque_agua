
import flet as ft
from colores import Colores


def crear_tanque(nivel, altura_maxima = 4.0):

    # Evitar que el nivel sea menor que 0 o mayor que 100
    nivel = max(0, min(100, nivel))

    # Calcular la altura del agua
    altura_agua = altura_maxima * nivel / 100

    # Calcular el tamaño visual del agua
    altura_visual = 220 * nivel / 100

    agua = ft.Container(
        width = 190,
        height = max(2, altura_visual),
        bgcolor = Colores["Turquesa"],
        border_radius = 35,
        alignment = ft.Alignment.CENTER,
        content = ft.Text(
            f"{altura_agua:.2f} m",
            size = 23,
            weight = ft.FontWeight.BOLD,
            color = Colores["Fondo"]
        )
    )

    tanque = ft.Container(
        width = 210,
        height = 240,
        padding = 5,
        border = ft.Border.all(2, Colores["Texto_Secundario"]),
        border_radius = 20,
        alignment = ft.Alignment.BOTTOM_CENTER,
        content = agua
    )

    return ft.Container(
        width = 280,
        padding = 15,
        bgcolor = Colores["Barra_lateral"],
        border_radius = 15,

        content = ft.Column(
            controls=[
                ft.Text(
                    "Nivel actual",
                    size = 16,
                    weight = ft.FontWeight.BOLD,
                    color = Colores["Texto"]
                ),

                ft.Text(
                    f"{nivel:.1f} %",
                    size = 30,
                    weight = ft.FontWeight.BOLD,
                    color = Colores["Texto"]
                ),

                ft.Container(
                    alignment = ft.Alignment.CENTER,
                    content = tanque
                ),

                ft.Text(
                    f"Rango operativo: 20 % - 90 %",
                    size = 11,
                    color = Colores["Texto_Secundario"]
                )
            ],
            spacing = 12
        )
    )
