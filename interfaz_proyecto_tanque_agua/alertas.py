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

def comprobar_alertas(nivel):
    if nivel < 20:
        return crear_alertas(
            "Nivel de agua por debajo del limite minimo",
            "El nivel del tanque se encuentra por debajo del 20%",
            ft.Icons.WARNING_AMBER,
            Colores["Nivel_Min"]
        )
    elif nivel > 90:
        return crear_alertas(
            "Nivel de agua por encima del limite maximo",
            "El nivel del tanque se encuentra por encima del 90%",
            ft.Icons.WARNING_AMBER,
            Colores["Nivel_Max"]
        )
    else:
        return crear_alertas(
            "Nivel de agua normal",
            "El nivel del tanque se encuentra en el rango permitido",
            ft.Icons.CHECK_CIRCLE,
            Colores["Turquesa"]
        )

def recomendacion_limpieza(ciclos, ciclos_maximos):
    if ciclos >= ciclos_maximos:
        return crear_alertas(
            "Limpieza recomendada",
            "Se han alcanzado los ciclos maximos. Se recomienda realizar una limpieza.",
            ft.Icons.BUILD,
            Colores["Nivel_Max"]
        )
