import flet as ft
from flet.controls import border

from colores import Colores

def crear_encabezado():
    encabezado = ft.Row(
        controls = [
            ft.Icon(ft.Icons.WATER_DROP, color = Colores["Turquesa"], size = 30),
            ft.Text("Acuarella", size = 20, weight = ft.FontWeight.BOLD, color = Colores["Texto"])
        ],
        spacing = 10,
        alignment = ft.MainAxisAlignment.CENTER
    )
    return encabezado

def encabezado_principal():
    encabezado_2 = ft.Column(
        controls = [
            ft.Text(
                "Monitoreo del tanque",
                size = 25,
                color =  Colores["Texto"],
            ),
            ft.Text(
                "Tanque principal",
                size = 15,
                color = Colores["Texto_Secundario"]
            )
        ],
        spacing = 5
    )
    return encabezado_2