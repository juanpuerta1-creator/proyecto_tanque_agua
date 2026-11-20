
import flet as ft
from colores import Colores


def crear_panel_temperatura(temperatura):

    # Determinar el estado de la temperatura
    if temperatura < 18:
        estado = "Temperatura baja"
        color_estado = "#20A9D2"

    elif temperatura <= 30:
        estado = "Temperatura normal"
        color_estado = Colores["Turquesa"]

    else:
        estado = "Temperatura alta"
        color_estado = "#FF5B3B"

    # Limitar el indicador visual entre 0 y 100
    porcentaje = max(0, min(100, temperatura * 2))

    return ft.Container(
        padding = 20,
        bgcolor = Colores["Barra_lateral"],
        border_radius = 15,
        expand = True,

        content = ft.Column(
            controls = [

                # Encabezado
                ft.Row(
                    controls = [
                        ft.Text(
                            "Temperatura del agua",
                            size = 16,
                            weight = ft.FontWeight.BOLD,
                            color = Colores["Texto"]
                        ),

                        ft.Icon(
                            ft.Icons.THERMOSTAT,
                            color = Colores["Turquesa"],
                            size = 25
                        )
                    ],
                    alignment = ft.MainAxisAlignment.SPACE_BETWEEN
                ),

                # Temperatura actual
                ft.Row(
                    controls = [
                        ft.Text(
                            f"{temperatura:.1f}",
                            size = 38,
                            weight = ft.FontWeight.BOLD,
                            color = Colores["Texto"]
                        ),

                        ft.Text(
                            "°C",
                            size = 20,
                            color = Colores["Turquesa"]
                        )
                    ],
                    vertical_alignment = ft.CrossAxisAlignment.CENTER,
                    spacing = 5
                ),

                # Indicador de temperatura
                ft.Container(
                    height = 10,
                    border_radius = 10,
                    bgcolor = Colores["Fondo"],
                    clip_behavior = ft.ClipBehavior.HARD_EDGE,

                    content = ft.Container(
                        width = porcentaje,
                        bgcolor = color_estado,
                        border_radius = 10
                    )
                ),

                # Estado
                ft.Row(
                    controls = [
                        ft.Icon(
                            ft.Icons.CIRCLE,
                            color = color_estado,
                            size = 10
                        ),

                        ft.Text(
                            estado,
                            size = 12,
                            color = color_estado,
                            weight = ft.FontWeight.BOLD
                        )
                    ],
                    spacing = 5
                ),

                ft.Text(
                    "Medición de temperatura del tanque principal",
                    size = 11,
                    color = Colores["Texto_Secundario"]
                )
            ],
            spacing = 12
        )
    )
